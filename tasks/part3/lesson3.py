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