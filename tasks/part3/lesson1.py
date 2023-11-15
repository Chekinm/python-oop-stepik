# class Point:
#     MAX_COORD = 100
#     MIN_COORD = 0
 
#     def __init__(self, x, y):
#         self.x = x
#         self.y = y

#     @property
#     def x(self):
#         return self.__x
    
#     @x.setter
#     def x(self, x):
#         self.__x = xtype

#     @property
#     def y(self):
#         return self.__y
    
#     @y.setter
#     def y(self, y):
#         self.__y = y
 
#     def __getattribute__(self, item):
#         if item == "2":
#             raise ValueError("Private attribute")
#         else:
#             return object.__getattribute__(self, item)
        
#     def __setattr__(self, key, value):
#         print('__setattr__', self, key, value)
#         if key == 'z':
#             raise AttributeError("недопустимое имя атрибута")
#         else:
#             object.__setattr__(self, key, value)

#     def __getattr__(self, item):
#         print("__getattr__: " + item)


# task 3 

# class Book:

#     def __init__(self, title: str = "",
#                  author: str = "",
#                  pages: int = 0,
#                  year: int = 0,
#                  ) -> None:
#         self.title = title
#         self.author = author
#         self.pages = pages
#         self.year = year

#     def __setattr__(self, attr: str, value: any) -> None:
#         if not isinstance(value, self.__init__.__annotations__[attr]):
#             raise TypeError("Неверный тип присваиваемых данных.")
#         object.__setattr__(self, attr, value)


# book = Book('Python ООП', 'Сергей Балакирев', 123, 2022)
# book = Book(True, 'Сергей Балакирев', 123, 2022)

# task 4
# from typing import Union


# class Product:
#     __counter = 0

#     def __new__(cls, *args, **kwargs):
#         cls.__counter += 1
#         return super().__new__(cls)

#     def __init__(self,
#                  name: str,
#                  weight: Union[int, float],
#                  price: Union[int, float],
#                  id: int = 0
#                  ) -> None:
#         self.id = self.__counter
#         self.name = name
#         self.weight = weight
#         self.price = price

#     def __setattr__(self, attr: str, value: any):
#          if ((attr in ('weight', 'price') and    
#              (not isinstance(value, (float, int)) or
#              value < 0)) or
#             (attr == 'name' and
#              not isinstance(value, str))):

#         # if not isinstance(value, self.__init__.__annotations__[attr]):
#             raise TypeError("Неверный тип присваиваемых данных.")
#         super().__setattr__(attr, value)

#     def __delattr__(self, attr: str) -> None:
#         if attr == 'id':
#             raise AttributeError("Атрибут id удалять запрещено.")
#         super().__delattr__(self, attr)


# class Shop:

#     def __init__(self, name: str) -> None:
#         self.name = name
#         self.goods = []

#     def add_product(self, product: Product) -> None:
#         self.goods.append(product)

#     def remove_product(self, product: Product) -> None:
#         self.goods.remove(product)

# shop = Shop("Балакирев и К")
# book = Product("Python ООП", 100, 1024)
# shop.add_product(book)
# shop.add_product(Product("Python", 150, 512))
# for p in shop.goods:
#     print(f"{p.name}, {p.weight}, {p.price}")


# print(book.__init__.__annotations__['weight'])

# # task 5

# from typing import Any


# class LessonItem:
#     def __init__(self,
#                  title: str,
#                  practices: int,
#                  duration: int,
#                  ):
#         self.title = title
#         self.practices = practices
#         self.duration = duration

#     def __setattr__(self, attr: str, value: Any) -> None:
#         if (not isinstance(value, self.__init__.__annotations__[attr]) or
#                 (self.__init__.__annotations__[attr] == int and value < 0)):
#             raise TypeError("Неверный тип присваиваемых данных.")
#         super().__setattr__(attr, value)

#     def __delattr__(self, attr: str) -> None:
#         if attr in self.__init__.__annotations__:
#             raise AttributeError(f"Атрибут {attr} aудалять запрещено.")
#         super().__delattr__(attr)

#     def __getattr__(self, attr: str) -> bool:
#         return False
    
#     def __str__(self):
#         return f'{self.title}. Duration {self.duration}, practices: {self.practices}'


# class Module:

#     def __init__(self, name) -> None:
#         self.name = name
#         self.lessons = []

#     def add_lesson(self, lesson: LessonItem):
#         self.lessons.append(lesson)

#     def remove_lesson(self, indx):
#         self.lessons.pop(indx)


# class Course:

#     def __init__(self, name) -> None:
#         self.name = name
#         self.modules = []

#     def add_module(self, module: Module):
#         self.modules.append(module)

#     def remove_module(self, indx):
#         self.modules.pop(indx)


# course = Course("Python ООП")
# module_1 = Module("Часть первая")
# module_1.add_lesson(LessonItem("Урок 1", 7, 1000))
# module_1.add_lesson(LessonItem("Урок 2", 10, 1200))
# module_1.add_lesson(LessonItem("Урок 3", 5, 800))
# course.add_module(module_1)
# module_2 = Module("Часть вторая")
# module_2.add_lesson(LessonItem("Урок 1", 7, 1000))
# module_2.add_lesson(LessonItem("Урок 2", 10, 1200))
# course.add_module(module_2)

# for module in course.modules:
#     for lesson in module.lessons:
#         print(f'{course.name}. {module.name}. {lesson}')
    
# # task 6

# from typing import Any

# class Picture:

#     def __init__(self, name, author, descr) -> None:
#         self.name = name
#         self.author = author
#         self.descr = descr


# class Mummies:
#     def __init__(self, name, location , descr):
#         self.name = name
#         self.location = location
#         self.descr = descr


# class Papyri:
#     def __init__(self, name, date, descr):
#         self.name = name
#         self.date = date
#         self.descr = descr


# class Museum:

#     def __init__(self, name):
#         self.name = name
#         self.exhibits = []

#     def add_exhibit(self, obj):
#         self.exhibits.append(obj)

#     def remove_exhibit(self, obj):
#         self.exhibits.remove(obj)

#     def get_info_exhibit(self, indx):
#         obj = self.exhibits[indx]
#         return f"Описание экспоната {obj.name}: {obj.descr}"

# p = Picture('myname', '2', 'dectr')
# print(p.descr)

# task 7

# from typing import Any, Union


# class AppVK:

#     def __init__(self):
#         self.name = 'ВКонтакте'


# class AppYouTube:

#     def __init__(self, memory_max):
#         self.name = 'YouTube'
#         self.memory_max = memory_max


# class AppPhone:

#     def __init__(self, phone_list=None):
#         self.name = 'Phone'
#         if phone_list is None:
#             self.phone_list = {}
#         else:
#             self.phone_list = phone_list.copy


# class SmartPhone:
    
#     def __init__(self, model: str) -> Any:
#         self.model = model
#         self.apps_dict = {}
#         self.apps = []

#     def add_app(self, app: Union[AppVK, AppYouTube, AppPhone]) -> None:
#         self.apps_dict.setdefault(type(app), app)
#         self.apps = self.apps_dict.values()

#     def remove_app(self, app: Union[AppVK, AppYouTube, AppPhone]) -> None:
#         if app in self.apps_dict:
#             self.apps_dict.pop(type(app))
#             self.apps = self.apps_dict.values()

#         else:
#             raise ValueError(f'{app.name} is not istalled')


# sm = SmartPhone("Honor 1.0")
# sm.add_app(AppVK())
# sm.add_app(AppVK())  # второй раз добавляться не должно

# sm.add_app(AppYouTube(2048))
# for a in sm.apps:
#     print(a.name)


# task 8

# from typing import Any, Self


# class Circle:

#     # def __setattr__(self, __name: str, __value: Any) -> None:
#     #     prefix = f'_{self.__class__.__name__}__'
#     #     var_name = __name[len(prefix):]
#     #     if var_name:
#     #         if not isinstance(__value, self.__init__.__annotations__[var_name]):
#     #             raise TypeError("Неверный тип присваиваемых данных.")
#     #         elif var_name == 'radius' and __value < 0:
#     #             pass

#     def __setattr__(self, __name: str, __value: Any) -> None:
#         print(__name, __value)
#         if __name in ('_Circle__x', '_Circle__y', '_Circle__radius'):
#             print('__ variable')
#             if not isinstance(__value, (float, int)):
#                 raise TypeError("Неверный тип присваиваемых данных.")
#             elif __name == '_Circle__radius' and __value < 0:
#                 print('negative radius')
#                 return
#         super().__setattr__(__name, __value)

#     def __getattr__(self, __name:str) -> bool:
#         return False

#     def __init__(self,
#                  x: float | int,
#                  y: float | int,
#                  radius: float | int):
#         self.x = x
#         self.y = y
#         self.radius = radius

#     @property
#     def x(self: Self) -> int| float:
#         return self.__x

#     @x.setter
#     def x(self, x: int | float) -> None:
#         self.__x = x

#     @property
#     def y(self: Self) -> int| float:
#         return self.__y

#     @y.setter
#     def y(self, y: int | float) -> None:
#         self.__y = y

#     @property
#     def radius(self: Self) -> int | float:
#         return self.__radius

#     @radius.setter
#     def radius(self, radius: int | float) -> None:
#         self.__radius = radius



# c = Circle(1,1, 22)
# c.radius = -22
# print(c.radius)

# task 9

# from typing import Any


# class FloatValue:

#     def __init__(self, __min, __max):
#         self.__min = __min
#         self.__max = __max

#     def __set_name__(self, owner, name):
#         self.name = '__' + name

#     def __get__(self, instance, owner):
#         return getattr(instance, self.name)

#     def __set__(self, instance, value):
#         if (isinstance(value, float) and
#                 self.__min <= value <= self.__max):
#             setattr(instance, self.name, value)
#         else:
#             return



# class Dimensions:
#     MIN_DIMENSION = 10
#     MAX_DIMENSION = 1000
#     a = FloatValue(MIN_DIMENSION, MAX_DIMENSION)
#     b = FloatValue(MIN_DIMENSION, MAX_DIMENSION)
#     c = FloatValue(MIN_DIMENSION, MAX_DIMENSION)

#     def __setattr__(self, __name: str, __value: Any) -> None:
#         if __name in ('MIN_DIMENSION','MAX_DIMENSION'):
#             raise AttributeError("Менять атрибуты MIN_DIMENSION и MAX_DIMENSION запрещено.")
#         super().__setattr__(__name, __value)

#     def __init__(self, a, b, c):
#         self.a = a
#         self.b = b
#         self.c = c

# task9 2 varianst

# from typing import Any


# class Dimensions:
#     MIN_DIMENSION = 10
#     MAX_DIMENSION = 1000


#     def __setattr__(self, __name: str, __value: Any) -> None:
#         if __name in ('MIN_DIMENSION','MAX_DIMENSION'):
#             raise AttributeError("Менять атрибуты MIN_DIMENSION и MAX_DIMENSION запрещено.")
#         super().__setattr__(__name, __value)

#     def __init__(self, a, b, c):
#         self.a = a
#         self.b = b
#         self.c = c

#     @property
#     def a(self):
#         return self.__a
    
#     @a.setter
#     def a(self, value):
#         if (isinstance(value, float) and
#                 self.MIN_DIMENSION <= value < self.MAX_DIMENSION):
#             self.__a = value

#     @property
#     def b(self):
#         return self.__b
    
#     @b.setter
#     def b(self, value):
#         if (isinstance(value, float) and
#                 self.MIN_DIMENSION <= value < self.MAX_DIMENSION):
#             self.__b = value
    
#     @property
#     def c(self):
#         return self.__c
    
#     @c.setter
#     def c(self, value):
#         if (isinstance(value, float) and
#                 self.MIN_DIMENSION <= value < self.MAX_DIMENSION):
#             self.__c = value


# # task 10

# import time
# from typing import Any


# class Filter:

#     def __setattr__(self, __name: str, __value: Any) -> None:
#         if __name == 'date' and self.date_lock:
#             return
#         else:
#             super().__setattr__(__name, __value)

#     def __init__(self, date):
#         self.date_lock = False
#         self.date = date
#         self.date_lock = True


# class Mechanical(Filter):
#     pass


# class Aragon(Filter):
#     pass


# class Calcium(Filter):
#     pass


# class GeyserClassic:

#     MAX_DATE_FILTER = 100 

#     FILTER_TYPE_DICT = {1: Mechanical,
#                         2: Aragon,
#                         3: Calcium,
#                         }

#     def __init__(self, 
#                  slot_1: Mechanical = None,
#                  slot_2: Aragon = None,
#                  slot_3: Calcium = None,
#                  ):
#         self.__slots_dict = {1: slot_1, 2: slot_2, 3: slot_3}

#     def add_filter(self, slot_num, filter):

#         if (type(filter) is self.FILTER_TYPE_DICT[slot_num] and
#                 self.__slots_dict[slot_num] is None):
#             self.__slots_dict[slot_num] = filter

#     def remove_filter(self, slot_num):
#         self.__slots_dict[slot_num] = None

#     def get_filters(self):
#         return tuple(self.__slots_dict[i] for i in range(1, 4))
    
#     def water_on(self):
#         for filter in self.__slots_dict.values():
#             if (filter is None or
#                     time.time() - filter.date > self.MAX_DATE_FILTER):
#                 return False
#         return True



