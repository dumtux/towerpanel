import asyncio
import json
from async_timeout import timeout
from serial_asyncio import open_serial_connection
from tornado.ioloop import IOLoop, PeriodicCallback
from tornado.web import Application
from tornado.web import RequestHandler as _RequestHandler
from tornado.websocket import WebSocketHandler as _WebSocketHandler, WebSocketClosedError


DEVICES = {
    'gps': {'dev': '/dev/ttyS1', 'baudrate': 115200, "timeout": 4},
    'rs232': {'dev': '/dev/ttyUSB1', 'baudrate': 9600, "timeout": 4},
    'rs485': {'dev': '/dev/ttyUSB0', 'baudrate': 9600, "timeout": 4},
    'uhf': {'dev': '/dev/ttyUSB2', 'baudrate': 19200, "timeout": 4},
    'test': {'dev': './ttyWriter', 'baudrate': 9600, "timeout": 4},
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

class BusConfig():

    def __init__(self, baudrate=9600, timeout=4):
        self.baudrate = baudrate
        self.timeout = timeout
        self.monitoring = True


###################
# Web Application #
###################


class SettingsHandler(RequestHandler):

    def post(self, device_name: str):
        body = json.loads(self.request.body.decode())
        print(body)
        for client in DeviceSocketHandler.clients:
            if client.device_name == device_name:
                client.current_config.baudrate = body["baudrate"]
                client.current_config.timeout = body["timeout"]
                client.current_config.monitoring = body["monitoring"]
                self.write({"message": "setting changed successfully."})
                return
        raise Exception(f"Not found device name {device_name}")


class DeviceSocketHandler(WebSocketHandler):
    """ WebSocket Handler for I/O forwarding """

    clients = set()

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.current_config = None
        self.port_reader = None
        self.port_writer = None
        self.port = None
        self.device_name = None

    def is_monitoring(self):
        return self.current_config.monitoring

    def open(self, device_name: str):
        setattr(self, 'is_open', True)
        self.device_name = device_name
        DeviceSocketHandler.clients.add(self)
        if self.current_config == None:
            self.current_config = BusConfig(
                baudrate=DEVICES[device_name]["baudrate"],
                timeout=DEVICES[device_name]["timeout"]
            )

        async def read_device():
            self.port_reader, self.port_writer = await open_serial_connection(
                url=DEVICES[device_name]['dev'], baudrate=DEVICES[device_name]['baudrate'])
            self.port = self.port_writer._transport.serial
            print(f"Connection to '{device_name}' is established.")

            while self.is_open:
                if self.current_config.baudrate != self.port.baudrate:
                    self.port.baudrate = self.current_config.baudrate

                if self.is_monitoring() == False:
                    await asyncio.sleep(0.5)
                    continue
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

    def on_message(self, tx_str: str):
        print(tx_str)
        tx_bytes = bytes(json.loads(tx_str))
        print(tx_bytes)
        print(f"{self.device_name} << {tx_str}")
        if self.current_config.baudrate != self.port.baudrate:
            self.port.baudrate = self.current_config.baudrate
        self.port_writer.write(tx_bytes)


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
