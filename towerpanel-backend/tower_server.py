import asyncio
import json

from async_timeout import timeout
from pydantic import BaseModel
from serial_asyncio import open_serial_connection
from tornado.ioloop import IOLoop, PeriodicCallback
from tornado.web import Application
from tornado.web import RequestHandler as _RequestHandler
from tornado.websocket import WebSocketHandler as _WebSocketHandler, WebSocketClosedError


DEVICES = {
    'gps': {'dev': '/dev/ttyS1', 'baud': 115200},
    'rs232': {'dev': '/dev/ttyUSB1', 'baud': 9600},
    'rs485': {'dev': '/dev/ttyUSB0', 'baud': 9600},
    'uhf': {'dev': '/dev/ttyUSB2', 'baud': 9600},
    'test': {'dev': './ttyWriter', 'baud': 9600},
}


#########################
# CORS enabled handlers #
#########################

class RequestHandler(_RequestHandler):
    """ CORS enabled RequestHandler """

    def set_default_headers(self):
        self.set_header("Content-Type", "application/json")
        self.set_header("Access-Control-Allow-Origin", "*")
        self.set_header("Access-Control-Allow-Headers", "content-type")
        self.set_header('Access-Control-Allow-Methods', 'POST, GET, OPTIONS, PATCH, PUT')

    def options(self, *args):
        self.set_status(204)
        self.finish()


class WebSocketHandler(_WebSocketHandler):
    """ CORS enabled WebSocketHandler """

    def check_origin(self, origin):
        return True


###############
# Data Models #
###############

class BusConfig(BaseModel):
    baudrate: int
    timeout: int


###################
# Web Application #
###################


class SettingsHandler(RequestHandler):

    def post(self, device_name: str):
        body = json.loads(self.request.body.decode())
        print(body)
        for client in DeviceSocketHandler.clients:
            client.current_config.baudrate = body["baudrate"]
            client.current_config.timeout = body["timeout"]
        self.write({"message": "setting changed successfully."})


class DeviceSocketHandler(WebSocketHandler):
    """ WebSocket Handler for I/O forwarding """

    clients = set()

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.current_config = BusConfig(baudrate=9600, timeout=4)
        self.port_reader = None
        self.port_writer = None
        self.port = None


    def open(self, device_name: str):
        setattr(self, 'is_open', True)
        DeviceSocketHandler.clients.add(self)

        async def read_device():
            self.port_reader, self.port_writer = await open_serial_connection(
                url=DEVICES[device_name]['dev'], baudrate=DEVICES[device_name]['baud'])
            self.port = self.port_writer._transport.serial
            print(f"Connection to '{device_name}' is established.")

            while self.is_open:
                if self.current_config.baudrate != self.port.baudrate:
                    self.port.baudrate = self.current_config.baudrate
                try:
                    async with timeout(self.current_config.timeout) as cm:
                        if self.port_reader == None:
                            print(f"Port for {device_name} is already closed.")
                            break
                        rx_bytes = await self.port_reader.readuntil(b'\n')
                        rx_str = json.dumps([int(b) for b in rx_bytes])
                        print(f"{device_name} >> {rx_str}")
                        try:
                            await self.write_message(rx_str)
                        except WebSocketClosedError:
                            print(f"WebSocket for {device_name} is already closed.")
                            break
                except asyncio.TimeoutError:
                    rx_bytes = b''
                    print(f"Timed Out while reading {device_name}")

            print(f"WebSocket for '{device_name}' is detached.")
        IOLoop.current().spawn_callback(read_device)

    def on_close(self):
        setattr(self, 'is_open', True)
        DeviceSocketHandler.clients.remove(self)
        self.port_reader = None
        self.port_writer = None

    def on_message(self, message):
        print(message)


def main():
    app = Application(
        [
            (r"/ws/(.*)", DeviceSocketHandler),
            (r"/bus/(.*)", SettingsHandler),
        ],
        websocket_ping_interval=10,
        websocket_ping_timeout=30,
    )
    app.listen(8000, '0.0.0.0')

    io_loop = IOLoop.current()
    io_loop.start()


if __name__ == "__main__":
    main()
