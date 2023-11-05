# class Point():
    

#     def __init__(self, x=0, y=0):
#         print('hi', )
#         self.x = x
#         self.y = y
#         print('hi2', self)

#     def __str__(self):
#         return f'Point with coord x={self.x} y={self.y}'


#     def set_coord(self, x, y):
#         self.x = x
#         self.y = y

#     def __del__(self):
#         print('deleting instantse of Point', self)


# pt = Point(1,2)
# print(pt)
# # print('before deletiion', pt)
# # pt = 5
# # print('after deletion', pt)

# # task 2

# class Money:
#     def __init__(self, money=0) -> None:
#         self.money = money

# task 3
# class Point:
#     def __init__(self, x, y, color='black') -> None:
#         self.x = x
#         self.y = y
#         self.color = color


# points = [Point(i, i) for i in range(1, 2000, 2)]
# points[1].color = 'yellow'

# 
# # task 5

# class TriangleChecker:

#     def __init__(self, a, b, c):
#         self.sides = [a,b,c]


#     def is_triangle(self):

#         for side in self.sides:
#             if type(side) not in (int, float) or side <= 0:
#                 return 1
#         sorted_sides = sorted(self.sides)
#         if sorted_sides[0] + sorted_sides[1] < sorted_sides[2]:
#             return 2

#         return 3


# # a, b, c = map(int, input().split())
# a, b, c = 1, 2, 3

# tr = TriangleChecker(a, b, c)

# print(tr.is_triangle())

# task 6

# class Graph:
#     def __init__(self, data, is_show=True):
#         self.data = data.copy()
#         self.is_show = is_show

#     def set_data(self, data):
#         self.data = data.copy

#     def set_show(self, is_show):
#         self.is_show = is_show

#     def _check_is_show(func):
#         def wrapper(self, *args, **kwargs):
#             if self.is_show:
#                 return func(self, *args, **kwargs)
#             else:
#                 print("Отображение данных закрыто")
#         return wrapper

#     def __str__(self):
#         return ' '.join(map(str, self.data))

#     @_check_is_show   # show_table = check_is_show(show_table)
#     def show_table(self):
#         print(self)

#     @_check_is_show
#     def show_graph(self):
#         print(f"Графическое отображение данных: {self}")

#     @_check_is_show
#     def show_bar(self):
#         print(f"Столбчатая диаграмма: {self}")


# data_graph = list(map(int, input().split()))

# gr = Graph(data_graph)

# gr.show_bar()
# gr.show_graph()
# gr.set_show(False)
# gr.show_table()

# # task 6 variant with @property decorator to get data s string
# # instead of using redefinition of __str__

# class Graph:
#     def __init__(self, data, is_show=True):
#         self.data = data.copy()
#         self.is_show = is_show

#     def set_data(self, data):
#         self.data = data.copy

#     def set_show(self, is_show):
#         self.is_show = is_show

#     def _check_is_show(func):
#         def wrapper(self, *args, **kwargs):
#             if self.is_show:
#                 return func(self, *args, **kwargs)
#             else:
#                 print("Отображение данных закрыто")
#         return wrapper
    
#     @property
#     def _data_as_string(self):
#         return ' '.join(map(str, self.data))

#     @_check_is_show   # show_table = check_is_show(show_table)
#     def show_table(self):
#         print(self._data_as_string)

#     @_check_is_show
#     def show_graph(self):
#         print(f"Графическое отображение данных: {self._data_as_string}")

#     @_check_is_show
#     def show_bar(self):
#         print(f"Столбчатая диаграмма: {self._data_as_string}")


# data_graph = list(map(int, input().split()))

# gr = Graph(data_graph)

# gr.show_bar()
# gr.show_graph()
# gr.set_show(False)
# gr.show_table()