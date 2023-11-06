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


# task 8
TYPE_OS = 1 # 1 -Window 2 linux

class DialogWindows:
    name_class = "DialogWindows"
    

class DialogLinux:
    name_class = "DialogLinux"


