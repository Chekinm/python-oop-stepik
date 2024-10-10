def integer_params(cls):
    methods = {k: v for k, v in cls.__dict__.items() if callable(v)}
    for k, v in methods.items():
        setattr(cls, k, integer_params_decorated(v))

    return cls


def integer_params_decorated(method):

    def wraped(self, *args, **kwargs):
        for arg in args:
            if not isinstance(arg, int):
                raise TypeError("аргументы должны быть целыми числами")
        for value in kwargs.values():
            if type(value) != 'int':
                raise TypeError("аргументы должны быть целыми числами")
        return method(self, *args, **kwargs)
    

    return wraped


@integer_params
class Vector:
    def __init__(self, *args):
        self.__coords = list(args)

    def __getitem__(self, item):
        return self.__coords[item]

    def __setitem__(self, key, value):
        self.__coords[key] = value

    def set_coords(self, *coords, reverse=False):
        c = list(coords)
        self.__coords = c if not reverse else c[::-1]