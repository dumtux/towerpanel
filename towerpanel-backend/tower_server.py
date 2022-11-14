import json
import random
from tornado.ioloop import IOLoop, PeriodicCallback
from tornado.web import Application
from tornado.web import RequestHandler as _RequestHandler
from tornado.websocket import WebSocketHandler as _WebSocketHandler


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


class SettingsHandler(RequestHandler):

    def post(self, device: str):
        body = json.loads(self.request.body.decode())
        print(body)
        self.write({"message": "setting changed successfully."})


class DeviceSocketHandler(WebSocketHandler):
    """ WebSocket Handler for I/O forwarding """

    # class variable
    clients = set()

    def open(self, device: str):
        print(f"Establishing connection to {device} ...")
        DeviceSocketHandler.clients.add(self)

    def on_close(self):
        DeviceSocketHandler.clients.remove(self)

    @classmethod
    def send_message(cls, message: str):
        print(f"Sending message {message} to {len(cls.clients)} client(s).")
        for client in cls.clients:
            client.write_message(message)


class RandomBernoulli:
    def __init__(self):
        self.p = 0.72
        print(f"True p = {self.p}")

    def sample(self):
        return int(random.uniform(0, 1) <= self.p)


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

    # Before starting the event loop, instantiate a RandomBernoulli and
    # register a periodic callback to write a sampled value to the WebSocket
    # every 100ms.
    random_bernoulli = RandomBernoulli()
    periodic_callback = PeriodicCallback(
        lambda: DeviceSocketHandler.send_message(str(random_bernoulli.sample())), 1000
    )
    periodic_callback.start()

    io_loop.start()


if __name__ == "__main__":
    main()
