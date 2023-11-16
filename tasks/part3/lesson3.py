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
