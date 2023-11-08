class Server:
    __count = 0

    def __new__(cls):
        cls.__count += 1
        return super().__new__(cls)

    def __init__(self) -> None:
        self.ip = self.__count
        self.__router = None
        self.buffer = []

    def get_ip(self):
        return self.ip

    def set_router(self, router):
        self.__router = router

    def unset_router(self):
        self.__router = None 

    def recieve_data(self, data):
        self.buffer.append(data)

    def get_data(self):
        response = self.buffer.copy()
        self.buffer.clear()
        return response

    def send_data(self, data):
        if self.__router:
            self.__router.recieve_message(data)
        else:
            pass
            # raise ConnectionAbortedError("server is not connected to any router")


class Router:

    __instance = None

    def __new__(cls, *args, **kwargs):
        if cls.__instance is None:
            cls.__instance = super().__new__(cls)
        return cls.__instance

    def __init__(self):
        self.__msg_buffer = []
        self.__server_network = {}

    def link(self, server):
        server.set_router(self)
        self.__server_network.setdefault(server.ip, server)

    def unlink(self, server):
        if self.__server_network.pop(server.ip, None) is None:
            pass
            # raise ConnectionAbortedError("server is not connected to any router")
        else:
            server.unset_router()

    def send_data(self):
        for msg in self.__msg_buffer:
            if msg.ip in self.__server_network:
                self.__server_network[msg.ip].recieve_data(msg)
            else:
                pass
                # raise ConnectionAbortedError("recepient is not connected to router")
        self.__msg_buffer.clear()

    def recieve_message(self, data):
        self.__msg_buffer.append(data)


class Data():
    def __init__(self, data, ip):
        self.data = data
        self.ip = ip


router = Router()
print(router)
sv_from = Server()
sv_from2 = Server()
router.link(sv_from)
router.link(sv_from2)
router.link(Server())
router.link(Server())
sv_to = Server()
router.link(sv_to)
sv_from.send_data(Data("Hello", sv_to.get_ip()))
sv_from2.send_data(Data("Hello", sv_to.get_ip()))
sv_to.send_data(Data("Hi", sv_from.get_ip()))
router.send_data()
msg_lst_from = sv_from.get_data()
msg_lst_to = sv_to.get_data()
print(msg_lst_from)
print(msg_lst_to)