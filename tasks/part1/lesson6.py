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


def singleton(cls):
    instances = {}

    def get_instance(*args, **kwargs):
        if cls not in instances:
            instances[cls] = cls(*args, **kwargs)
        return instances[cls]

    return get_instance

@singleton
class Singleton:
    def __init__(self, name):
        self.name = name

# Example usage:
singleton_instance_1 = Singleton('s')
singleton_instance_2 = Singleton('w')

print(singleton_instance_1 is singleton_instance_2)  # Should print True
print(singleton_instance_1.name)
print(singleton_instance_2.name)