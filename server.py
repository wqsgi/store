import asyncio
from store import Store

__author__ = 'weiqisong'


class Server(asyncio.Protocol):
    def __init__(self):
        super(Server).__init__()
        self.id = -1
        self.dc = ""
        self.ip = ""
        self.port = -1
        self.is_leader = False
        self.replica_group = -1
        self.follower_addr = []
        self.store = None

        self.state = -1

    def start(self):
        loop = asyncio.get_event_loop()
        server = loop.run_until_complete(loop.create_server(Server, 'localhost', 2222))
        loop.run_until_complete(server.wait_closed())

    def connection_made(self, transport):
        """
        Called when a connection is made.
        The argument is the transport representing the pipe connection.
        To receive data, wait for data_received() calls.
        When the connection is closed, connection_lost() is called.
        """
        print("Connection received!")
        self.transport = transport

    def data_received(self, data):
        """
        Called when some data is received.
        The argument is a bytes object.
        """
        print(data)
        self.transport.write(b'echo:')
        self.transport.write(data)

    def connection_lost(self, exc):
        """
        Called when the connection is lost or closed.
        The argument is an exception object or None (the latter
        meaning a regular EOF is received or the connection was
        aborted or closed).
        """
        print("Connection lost! Closing server...")
        server.close()

server = Server()
server.start()

