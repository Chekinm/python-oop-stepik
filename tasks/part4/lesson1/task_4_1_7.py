class Singleton:

    _instance = {}
    _singleton_name = None

    def __new__(cls, *arg, **kwarg):
        if cls.__name__ not in cls._instance:
            cls._instance[cls.__name__] = super().__new__(cls)
        return cls._instance[cls.__name__]


class Game(Singleton):

    def __init__(self, name):
        if 'name' not in self.__dict__:
            self.name = name

s = Singleton()
a = Game('sss')
b = Game('sgggg')
print(s.name)