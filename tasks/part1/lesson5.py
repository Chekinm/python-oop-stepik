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

# # task 7

# class CPU:
#     def __init__(self, name, fr):
#         self.name = name
#         self.fr = fr


# class Memory:
#     def __init__(self, name, volume):
#         self.name = name
#         self.volume = volume


# class MotherBoard:

#     def __init__(self, name, cpu, *mem_slots, total_mem_slots=4):
#         self.name = name
#         self.cpu = cpu
#         self.mem_slots = list(mem_slots)
#         self.total_mem_slots = total_mem_slots

#     @property
#     def memory_description(self):
#         mem_desc_list = [f'{m.name} - {m.volume}' for m in self.mem_slots]
#         return '; '.join(mem_desc_list)

#     def get_config(self):
#         return [f'Материнская плата: {self.name}',
#                 f'Центральный процессор: {cpu.name}, {cpu.fr}',
#                 f'Слотов памяти: {self.total_mem_slots}',
#                 f'Память: {self.memory_description}',
#                 ]


# cpu = CPU('my_cpu', 100)
# mem1 = Memory('mem1', 10)
# mem2 = Memory('mem2', 20)

# mb = MotherBoard('my_motherboard', cpu, mem1, mem2)

# # task 8

# class Cart:
#     def __init__(self) -> None:
#         self.goods = []

#     def add(self, gd):
#         self.goods.append(gd)

#     def remove(self, indx):
#         try:
#             self.goods.pop(indx)
#         except IndexError:
#             print('Looks the index is out of range,',
#                   '\n',
#                   'Should be greather than 0'
#                   f'and not less than {len(self.goods)}')

#     def get_list(self):
#         return [str(gd) for gd in self.goods]


# class Goods:
#     def __init__(self, name, price) -> None:
#         self.name = name
#         self.price = price
    
#     def __str__(self):
#         return f'{self.name}: {self.price}'


# class Table(Goods):
#     pass


# class TV(Goods):
#     pass


# class Notebook(Goods):
#     pass


# class Cup(Goods):
#     pass


# cart = Cart()

# tv1 = TV("samsung", 1111)
# tv2 = TV("LG", 1234)
# table = Table("ikea", 2345)
# n1 = Notebook("msi", 5433)
# n2 = Notebook("apple", 542)
# c = Cup("keepcup", 43)

# cart.add(tv1)
# cart.add(tv2)
# cart.add(table)
# cart.add(n1)
# cart.add(n2)
# cart.add(c)

# print(cart.get_list())

# task 9

# 

# # task 10

# from random import randint


# class Cell:
#     def __init__(self, mine, around_mines=0, fl_open=False):
#         self.mine = mine
#         self.around_mines = around_mines
#         self.fl_open = fl_open

#     def __str__(self):
#         if not self.fl_open:
#             return '#'
#         if self.mine:
#             return '*'
#         return f'{self.around_mines}'


# class GamePole:

#     def __init__(self, n, m):
#         self.size = n
#         self.mines = m
#         self.pole = [[Cell(False) for _ in range(self.size)] for _ in range(self.size)]
#         self.init()

#     def _set_around(self, x, y):
#         for _x in range(x - 1, x + 2, 1):
#             for _y in range(y - 1, y + 2, 1):
#                 if 0 <= _x < self.size and 0 <= _y < self.size:
#                     self.pole[_x][_y].around_mines += 1

#     def init(self):
#         mines = self.mines
#         while mines > 0:
#             x = randint(0, self.size - 1)
#             y = randint(0, self.size - 1)
#             if not self.pole[x][y].mine:
#                 self.pole[x][y].mine = True
#                 self._set_around(x, y)
#                 mines -= 1

#     def show(self):
#         for _ in range(self.size):
#             print(*self.pole[_])


# gp = GamePole(10, 12)
# gp.show()
