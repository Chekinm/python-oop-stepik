#  task 2
# class Record:

#     def __init__(self, **fields):
#         self.ind_to_keys = {i: key for i, key in enumerate(fields.keys())}
#         for key, value in fields.items():
#             self.__setattr__(key, value)

#     def __getitem__(self, ind):
#         try: 
#             return self.__getattribute__(self.ind_to_keys[ind])
#         except KeyError:
#             raise IndexError('неверный индекс поля')

#     def __setitem__(self, ind, value):
#         try:
#             self.__setattr__(self.ind_to_keys[ind], value)
#         except KeyError:
#             raise IndexError('неверный индекс поля')

# r = Record(pk=1, title='Python ООП', author='Балакирев')

# print(r.pk) # 1)
# print(r.title) # Python ООП)
# print(r.author) # Балакирев)

# for i in range(4):
#     try:
#         print(r[i])
#     except IndexError:
#         print("Index not found")

# # task 3

# class Track:

#     def __init__(self, start_x: int,  start_y: int):
#         self.start_x = start_x
#         self.start_y = start_y
#         self.points  = []

#     def add_point(self, x, y, speed):
#         self.points .append([(x, y), speed])

#     def __getitem__(self, ind):
#         try:
#             return self.points[ind]
#         except IndexError:
#             raise IndexError('некорректный индекс')

#     def __setitem__(self, ind, speed):
#         try:
#             self.points[ind][-1] = speed
#         except IndexError:
#             raise IndexError('некорректный индекс')

# task 4

