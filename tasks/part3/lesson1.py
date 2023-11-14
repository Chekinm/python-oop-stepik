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
from typing import Union


class Product:
    __counter = 0

    def __new__(cls, *args, **kwargs):
        cls.__counter += 1
        return super().__new__(cls)

    def __init__(self,
                 name: str,
                 weight: Union[int, float],
                 price: Union[int, float],
                 id: int = 0
                 ) -> None:
        self.id = self.__counter
        self.name = name
        self.weight = weight
        self.price = price

    def __setattr__(self, attr: str, value: any):
        if ((attr in ('weight', 'price') and
             not isinstance(value, (float, int))) or
            (attr == 'name' and
             not isinstance(value, str))):
        # if not isinstance(value, self.__init__.__annotations__[attr]):
            raise TypeError("Неверный тип присваиваемых данных.")
        super().__setattr__(attr, value)

    def __delattr__(self, attr: str) -> None:
        if attr == 'id':
            raise AttributeError("Атрибут id удалять запрещено.")
        super().__delattr__(self, attr)


class Shop:

    def __init__(self, name: str) -> None:
        self.name = name
        self.goods = []

    def add_product(self, product: Product) -> None:
        self.goods.append(product)

    def remove_product(self, product: Product) -> None:
        self.goods.remove(product)





shop = Shop("Балакирев и К")
book = Product("Python ООП", 100, 1024)
shop.add_product(book)
shop.add_product(Product("Python", 150, 512))
for p in shop.goods:
    print(f"{p.name}, {p.weight}, {p.price}")


print(book.__init__.__annotations__['weight'])





    

