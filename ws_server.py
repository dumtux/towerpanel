import asyncio
import json
from pprint import pprint
import serial_asyncio
from fastapi import FastAPI, WebSocket
from fastapi.responses import HTMLResponse


app = FastAPI()

html = """
<!DOCTYPE html>
<html>
    <head>
        <title>Chat</title>
    </head>
    <body>
        <h1>WebSocket Chat</h1>
        <form action="" onsubmit="sendMessage(event)">
            <input type="text" id="messageText" autocomplete="off"/>
            <button>Send</button>
        </form>
        <ul id='messages'>
        </ul>
        <script>
            var ws = new WebSocket(location.origin.replace(/^http/, 'ws') + "/ws");
            ws.onmessage = function(event) {
                var messages = document.getElementById('messages')
                var message = document.createElement('li')
                var content = document.createTextNode(event.data)
                message.appendChild(content)
                messages.appendChild(message)
                if (messages.childElementCount > 10) {
                    messages.removeChild(messages.firstElementChild);
                }
            };
            function sendMessage(event) {
                var input = document.getElementById("messageText")
                ws.send(input.value)
                input.value = ''
                event.preventDefault()
            }
        </script>
    </body>
</html>
"""


@app.get("/")
async def get():
    return HTMLResponse(html)


@app.websocket("/ws")
async def websocket_endpoint(websocket: WebSocket):
    await websocket.accept()
    uart_rx, uart_tx = await serial_asyncio.open_serial_connection(url='/dev/ttyS1', baudrate=115200)

    async def read_from_socket(websocket: WebSocket):
        while True:
            tx_str = await websocket.receive_text()
            tx_str += '\n'
            tx_bytes = tx_str.encode()
            uart_tx.write(tx_bytes)
            print(tx_bytes)

    asyncio.create_task(read_from_socket(websocket))

    while True:
        rx_bytes = await uart_rx.readuntil(b'\n')
        try:
            data = {"gnss_rx": rx_bytes.decode(), "gnss_rx_type": "string"}
        except UnicodeDecodeError:
            data = {"gnss_rx": f"{rx_bytes}", "gnss_rx_type": "bytes"}
        await websocket.send_text(json.dumps(data))
        pprint(data)
