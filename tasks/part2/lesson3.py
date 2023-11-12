# # task 6

# class FloatValue():

#     def __set_name__(self, owner, name):
#         self.name = '_' + name

#     def __get__(self, instance, owner):
#         return getattr(instance, self.name)

#     def __set__(self, instance, value):
#         if isinstance(value, float):
#             setattr(instance, self.name, value)
#         else:
#             raise TypeError("Присваивать можно только вещественный тип данных.")

# class Cell:
#     value = FloatValue()

#     def __init__(self, value):
#         self.value = value

#     def __repr__(self):
#         return f'{self.value}'


# class TableSheet:

#     def __init__(self, N, M):
#         self.cells = [[Cell(0.0) for _ in range(N)] for _ in range(M)]


# N = 3
# M = 5
# table = TableSheet(N, M)

# for i in range(15):
#     table.cells[i//N][i%N].value = i / 1 + 1

# print(table.cells)

