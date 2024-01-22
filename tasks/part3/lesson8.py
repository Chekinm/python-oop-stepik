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

# # task 5

# class IntegerValue:

#     def __set_name__(self, owner, name):
#         self.name = f'_{owner.__name__}__{name}'

#     def __get__(self, instance, owner=None):
#         if instance is not None:
#             return getattr(instance, self.name)
#         return None

#     def __set__(self, instance, value):
#         if isinstance(value, int):
#             setattr(instance, self.name, value)
#         else:
#             raise ValueError('возможны только целочисленные значения')

#     def __delete__(self, instance):
#         if instance is not None:
#             delattr(instance, self.name)
#         return None


# class CellInteger:
#     value = IntegerValue()

#     def __init__(self, start_value=0):
#         self.value = start_value

#     def __str__(self):
#         return str(self.value)




# class TableValues:
    
#     def __init__(self, rows, cols, cell=None):
#         if cell is not None:
#             self.cells = tuple([tuple([cell() for i in range(cols)]) for j in range(rows)])

#         else:
#             raise ValueError('параметр cell не указан')
        
#     def __getitem__(self, ind):
#         row, col = ind
#         try:
#             return self.cells[row][col].value
#         except IndexError:
#             raise IndexError('one of index is out of range')
    
#     def __setitem__(self, ind, value):
#         row, col = ind
#         try:
#             self.cells[row][col].value = value
#         except IndexError:
#             raise IndexError('one of index is out of range')



# a = CellInteger(5)
# print(a.value)
# t = TableValues(4, 3, cell=CellInteger)
# t[1, 2] = 10
# print(t[1, 2])


# # task 6

# class StackObj:

#     def __init__(self, data):
#         self.data = data
#         self.next = None

# class Stack:

#     def __init__(self):
#         self.top = None
#         self.length = 0
        
#     def __len__(self):
#         return self.length

#     def push(self, st_obj):
#         st_obj.next = self.top
#         self.top = st_obj
#         self.length += 1

#     def pop(self):
#         res = self.top
#         self.top = self.top.next
#         self.length -= 1
#         return res

#     def __getitem__(self, ind):
#         if isinstance(ind, int) and 0 <= ind < self.length:
#             res = self.top
#             for i in range(self.length - 1, ind, -1):
#                 res = res.next
#             return res
#         else:
#             raise IndexError('неверный индекс') 
        
#     def __setitem__(self, ind, new_obj):
#         if isinstance(ind, int) and 0 <= ind < self.length:
#             res = self.top
#             for i in range(self.length - 1, ind, -1):
#                 res = res.next
#             res.data = new_obj.data
#         else:
#             raise IndexError('неверный индекс') 
        

# st = Stack()
# st.push(StackObj("obj11"))
# st.push(StackObj("obj12"))
# st.push(StackObj("obj13"))
# st[1] = StackObj("obj2-new")
# assert st[0].data == "obj11" and st[1].data == "obj2-new", "атрибут data объекта класса StackObj содержит неверные данные"

# try:
#     obj = st[3]
# except IndexError:
#     assert True
# else:
#     assert False, "не сгенерировалось исключение IndexError"

# obj = st.pop()
# assert obj.data == "obj13", "метод pop должен удалять последний объект стека и возвращать его"

# n = 0
# h = st.top
# while h:
#     assert isinstance(h, StackObj), "объект стека должен быть экземпляром класса StackObj"
#     n += 1
#     h = h.next
# print(n)
# assert n == 2, "неверное число объектов в стеке (возможно, нарушена его структура)"

# # task 7

# class RadiusVector:

#     def __init__(self, *coords):
#         self.coords = list(coords)

#     def __getitem__(self, ind):
#         res = self.coords[ind]
#         return res if isinstance(res, int) else tuple(res)

#     def __setitem__(self, ind, value):
#         self.coords[ind] = value

# task 8 