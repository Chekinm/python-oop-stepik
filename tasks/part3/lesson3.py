# # task 2

# import sys
# class Book:

#     def __init__(self, title: str, author: str, pages: int) -> None:
#         print(title, author, pages)
#         self.title = title
#         self.author = author
#         self.pages = pages

#     def __str__(self) -> str:
#         return f'Книга: {self.title}; {self.author}; {self.pages}'


# lst_in = list(map(str.strip, sys.stdin.readlines()))

# b = Book(*lst_in)


# print(b)

# # task 3

# class Model:

#     def __init__(self):
#         self.data = {}

#     def query(self, **kwargs):
#         self.data = kwargs

#     def __str__(self):
#         if self.data:
#             return f'Model: {", ".join(f"{key} = {value}" for key, value in self.data.items())}'

#         return 'Model'


# model = Model()
# model.query(a=1, b=2)
# print(model)

# class WordString:

#     def __init__(self, string=""):
#         self.__words = []
#         self.string = string


#     @property
#     def string(self):
#         return self.__string

#     @string.setter
#     def string(self, string):
#         self.__string = string
#         self.__words = list(string.split())

#     def __len__(self):
#         return len(self.__words)

#     def __call__(self, indx):
#         try:
#             return self.__words[indx]
#         except IndexError:
#             print(f'index {indx} is out of range')
#         except TypeError: 
#             print(f'index {indx} is not a number')
        
# words = WordString()
# words.string = "Курс по Python ООП"
# n = len(words)
# first = "" if n == 0 else words(0)
# print(words.string)
# print(f"Число слов: {n}; первое слово: {first}")
# words(None)

# task 5

# class ObjList:

#     def __init__(self, data):
#         self.__data = data
#         self.next = None
#         self.prev = None

#     @property
#     def data(self):
#         return self.__data
    
#     @property
#     def next(self):
#         return self.__next
    
#     @next.setter
#     def next(self, obj):
#         self.__next = obj

#     @property
#     def prev(self):
#         return self.__prev
    
#     @prev.setter
#     def prev(self, obj):
#         self.__prev = obj
    



# class LinkedList:

#     def __init__(self):
#         self.head = None
#         self.tail = None
#         self.__lenght = 0

#     def add_obj(self, obj):
#         obj.prev = self.tail

#         if self.tail:
#             self.tail.next = obj
#         self.tail = obj
#         if self.head is None:
#             self.head = obj

#         self.__lenght += 1

#     def get_obj_by_indx(self, indx):
#         if not (0 <= indx < self.__lenght):
#             raise IndexError(f'Index {indx} is out of range')

#         else:
#             obj = self.head
#             i = 0
#             while obj and i < indx:
#                 obj = obj.next
#                 i += 1
#             return obj

#     def remove_obj(self, indx):

#         obj = self.get_obj_by_indx(indx)

#         prev, next = obj.prev, obj.next

#         if prev:
#             prev.next = next

#         if next:
#             next.prev = prev

#         if obj == self.head:
#             self.head = next

#         if obj == self.tail:
#             self.tail = prev
        
#         self.__lenght -= 1

#     def __call__(self, indx):
#         return self.get_obj_by_indx(indx).data

#     def __len__(self):
#         return self.__lenght

# linked_lst = LinkedList()
# linked_lst.add_obj(ObjList("Sergey"))
# linked_lst.add_obj(ObjList("Balakirev"))
# linked_lst.add_obj(ObjList("Python"))
# print(len(linked_lst))
# linked_lst.remove_obj(2)
# linked_lst.add_obj(ObjList("Python ООП"))
# n = len(linked_lst)  # n = 3
# s = linked_lst(1) # s = Balakirev
# print(s)

# # task 6
# from typing import Any
# from math import sqrt


# class Complex:

#     def __setattr__(self, __name: str, __value: Any) -> None:
#         if not isinstance(__value, (int, float)):
#             raise ValueError("Неверный тип данных.") 
#         else:
#             super().__setattr__(__name, __value)

#     def __init__(self, real, img):
#         self.real = real
#         self.img = img

#     @property
#     def real(self):
#         return self.__real

#     @real.setter
#     def real(self, value):
#         self.__real = value

#     @property
#     def img(self):
#         return self.__img

#     @img.setter
#     def img(self, value):
#         self.__img = value

#     def __abs__(self):
#         return sqrt(self.real*self.real + self.img*self.img)


# cmp = Complex(7, 8)
# cmp.real = 3
# cmp.img = 4
# c_abs = abs(cmp)


