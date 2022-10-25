import asyncio
import json
from pprint import pprint
import serial_asyncio
from fastapi import FastAPI, WebSocket
from fastapi.responses import HTMLResponse
import uvicorn


DEVICES = {
    'gps': {'dev': '/dev/ttyS1', 'baud': 115200},
    'rs232': {'dev': '/dev/ttyUSB1', 'baud': 9600},
    'rs485': {'dev': '/dev/ttyUSB0', 'baud': 9600},
    'uhf': {'dev': '/dev/ttyUSB2', 'baud': 9600},
    'test': {'dev': './ttyWriter', 'baud': 9600},
}

app = FastAPI()

@app.get("/")
async def get():
    return "WebSocket Dev server"


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
            writer.write(tx_bytes)

    asyncio.create_task(read_from_socket(websocket))

    while True:
        rx_bytes = await reader.readuntil(b'\n')
        rx_str = json.dumps([int(b) for b in rx_bytes])
        print(f"{device_name} >> {rx_str}")
        await websocket.send_text(rx_str)


if __name__=="__main__":
    uvicorn.run(app, host='0.0.0.0', port=8000)
