import asyncio
import json
from pprint import pprint
import serial_asyncio
from fastapi import FastAPI, WebSocket
from fastapi.responses import HTMLResponse
import subprocess
import uvicorn

app = FastAPI()

@app.get("/")
async def get():
    return "WebSocket Dev server"


@app.websocket("/ws")
async def websocket_endpoint(websocket: WebSocket):
    await websocket.accept()
    uart_rx, uart_tx = await serial_asyncio.open_serial_connection(url='/dev/ttyS1', baudrate=115200)

    async def read_from_socket(websocket: WebSocket):
        while True:
            tx_str = await websocket.receive_text()
            data = json.loads(tx_str)
            if "gnss_tx" in data.keys():
                tx_bytes = data["gnss_tx"].encode()
                uart_tx.write(tx_bytes)
                print(f"Sent >> {tx_bytes}")
            else:
                pprint(data)

    asyncio.create_task(read_from_socket(websocket))

    while True:
        rx_bytes = await uart_rx.readuntil(b'\n')
        try:
            data = {"gnss_rx": rx_bytes.decode(), "gnss_rx_type": "string"}
        except UnicodeDecodeError:
            data = {"gnss_rx": f"{rx_bytes}", "gnss_rx_type": "bytes"}
        await websocket.send_text(json.dumps(data))
        pprint(data)


if __name__=="__main__":
    uvicorn.run(app, host='0.0.0.0', port=8000)
