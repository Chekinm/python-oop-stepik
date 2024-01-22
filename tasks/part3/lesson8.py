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

# # task 4

# class Integer:

#     def __init__(self, value=0):
#         self.value = value

#     @property
#     def value(self):
#         return self.__value
    
#     @value.setter
#     def value(self, value):
#         if isinstance(value, int):
#             self.__value = value
#         else:
#             raise ValueError('должно быть целое число')
    
#     def __str__(self):
#         return str(self.value)


# class Array:

#     def __init__(self, max_length, cell=Integer):
#         self.array = [cell() for _ in range(max_length)]
#         self.max_length = max_length
    
#     def __len__(self):
#         return self.max_length
    
#     def __getitem__(self, ind):
#         if 0 <= ind <= self.max_length:
#             return self.array[ind].value
#         else:
#             raise IndexError('неверный индекс для доступа к элементам массива')
    
#     def __setitem__(self, ind, value):
#         if 0 <= ind <= self.max_length:
#             self.array[ind].value = value 
#         else:
#             raise IndexError('неверный индекс для доступа к элементам массива')
    
#     def __str__(self):
#         return ' '.join((str(self.array[i]) for i in range(self.max_length)))


# a = Integer(5)
# print(a)
# ar_int = Array(10, cell=Integer)
# print(ar_int[3])
# print(ar_int) # должны отображаться все значения массива в одну строчку через пробел
# ar_int[1] = 10
# try:
#     ar_int[1] = 10.5 # должно генерироваться исключение ValueError
# except ValueError as e:
#     print(e)
# try:
#     ar_int[10] = 1 # должно генерироваться исключение ValueError
# except IndexError as e:
#     print(e)

# print(ar_int)

# a = Array(20, cell=Integer)
# print(a[18]), "начальные значения в ячейках массива (в объектах класса Integer) должны быть равны 0"

# task 5

class 