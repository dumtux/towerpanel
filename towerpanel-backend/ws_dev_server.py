import asyncio
from async_timeout import timeout
import json
from pprint import pprint
import serial_asyncio
from fastapi import FastAPI, WebSocket, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import HTMLResponse
from pydantic import BaseModel
import uvicorn


DEVICES = {
    'gps': {'dev': '/dev/ttyS1', 'baud': 115200},
    'rs232': {'dev': '/dev/ttyUSB1', 'baud': 9600},
    'rs485': {'dev': '/dev/ttyUSB0', 'baud': 9600},
    'uhf': {'dev': '/dev/ttyUSB2', 'baud': 9600},
    'test': {'dev': './ttyWriter', 'baud': 9600},
}


class BusConfig(BaseModel):
    baudrate: int
    timeout: int


current_config = BusConfig(baudrate=9600, timeout=4)

app = FastAPI()
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"]
)


@app.get("/")
async def home():
    return "WebSocket Dev server"


@app.put("/bus/{device_name}")
async def update_item(device_name: str, config: BusConfig):
    if device_name not in DEVICES.keys():
        raise HTTPException(status_code=404, detail=f"`{device_name}` does not exist.")
    current_config.baudrate = config.baudrate
    current_config.timeout = config.timeout


@app.websocket("/ws/{device_name}")
async def websocket_gps(websocket: WebSocket, device_name: str):
    await websocket.accept()
    if device_name not in DEVICES.keys():
        print(f"Unknown device name '{device_name}'")
        return

    reader, writer = await serial_asyncio.open_serial_connection(
        url=DEVICES[device_name]['dev'], baudrate=DEVICES[device_name]['baud'])
    print(f"Connection to '{device_name}' is established.")

    async def read_from_socket(websocket: WebSocket):
        while True:
            tx_str = await websocket.receive_text()
            tx_bytes = bytes(json.loads(tx_str))
            print(f"{device_name} << {tx_str}")
            if current_config.baudrate != writer._transport.serial.baudrate:
                writer._transport.serial.baudrate = current_config.baudrate
            print(writer._transport.serial)
            writer.write(tx_bytes)

    asyncio.create_task(read_from_socket(websocket))

    while True:
        if current_config.baudrate != writer._transport.serial.baudrate:
            writer._transport.serial.baudrate = current_config.baudrate
        try:
            async with timeout(current_config.timeout) as cm:
                rx_bytes = await reader.readuntil(b'\n')
                rx_str = json.dumps([int(b) for b in rx_bytes])
                print(f"{device_name} >> {rx_str}")
                await websocket.send_text(rx_str)
        except asyncio.TimeoutError:
            rx_bytes = b''
            print("Timed Out listening {device_name}")


if __name__=="__main__":
    uvicorn.run(app, host='0.0.0.0', port=8000)
