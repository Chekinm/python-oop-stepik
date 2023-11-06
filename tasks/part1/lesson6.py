# # # task 6

# # class AbstractClass:

# #     def __new__(cls, *arg, **kwarg):
# #         return f'Ошибка: нельзя создавать объекты абстрактного класса'

# # task 7

# class SingletonFive:
#     __count = 0
#     __instance = None

#     def __new__(cls, *arg, **kwarg):
#         if cls.__count > 4:
#             return cls.__instance

#         cls.__instance = super().__new__(cls)
#         cls.__count += 1
#         return cls.__instance

#     def __init__(self, name):
#         self.name = name


# objs = [SingletonFive(str(n)) for n in range(10)]


# # task 8
# TYPE_OS = 1  # 1 -Window 2 linux


# class DialogMeta(type):
#     def __call__(cls, *args, **kwargs):
#         if TYPE_OS == 1:
#             return DialogWindows(*args, **kwargs)
#         else:
#             return DialogLinux(*args, **kwargs)


# class DialogWindows:
#     name_class = "DialogWindows"

#     def __init__(self, name):
#         print('call win init')
#         self.name = name


# class DialogLinux:
#     name_class = "DialogLinux"

#     def __init__(self, name):
#         print('call lin init')
#         self.name = name


# class Dialog(metaclass=DialogMeta):
#     pass


# TYPE_OS = 1
# dlg_1 = Dialog("123")
# TYPE_OS = 2
# dlg_2 = Dialog("1234")

# assert isinstance(dlg_1, DialogWindows) and isinstance(dlg_2, DialogLinux), "создаваемые объекты не соответствуют нужным классам DialogWindows или DialogLinux"

# assert dlg_1.name == "123", "неверное значение локального атрибута name класса DialogWindows"
# assert dlg_2.name == "1234", "неверное значение локального атрибута name класса DialogLinux"

# d1 = Dialog("12")
# d2 = Dialog("123")

# assert d1.name == "12" and d2.name == "123", "неверные значения в локальных атрибутах name разных объектов класса DialogLinux"

# task 10

class Factory:

    def build_sequence(self):
        self.sequence = []
        return self.sequence

    def build_number(self, string):
        float_number = float(string)
        return float_number


class Loader:
    def parse_format(self, string, factory):
        seq = factory.build_sequence()
        for sub in string.split(","):
            item = factory.build_number(sub)
            seq.append(item)

        return seq


# эти строчки не менять!
ld = Loader()
s = input()
res = ld.parse_format(s, Factory())

print(res)
