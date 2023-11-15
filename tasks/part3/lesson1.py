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

