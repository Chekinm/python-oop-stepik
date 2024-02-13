## task 5
# class Person:
#     __iteration_list = ('fio', 'job', 'old', 'salary', 'year_job')

#     def __init__(self, fio, job, old, salary, year_job):
#         self.fio = fio
#         self.job = job
#         self.old = old
#         self.salary = salary
#         self.year_job = year_job
#         self.iteration_step = 0

#     def __getitem__(self, idx):
#         try:
#             return getattr(self, self.__iteration_list[idx])
#         except (IndexError, TypeError):
#             raise IndexError('неверный индекс')

#     def __setitem__(self, idx, value):
#         try:
#             setattr(self, self.__iteration_list[idx], value)
#         except (IndexError, TypeError):
#             raise IndexError('неверный индекс')

#     def __iter__(self):
#         self.iteration_step = 0
#         return self

#     def __next__(self):
#         try:
#             next_value = self[self.iteration_step]
#             self.iteration_step += 1
#             return next_value
#         except IndexError:
#             raise StopIteration




# pers = Person('Гейтс Б.', 'бизнесмен', 61, 1000000, 46)
# #pers.fio = 1

# for i in pers:
#     print(i)

# # task 6

# class TriangleListIterator:

#     def __init__(self, lst):
#         self.lst = lst
#         self.x_iter = 0
#         self.y_iter = 0

#     def __iter__(self):
#         self.x_iter = 0
#         self.y_iter = 0
#         return self

#     def __next__(self):
#         try:
#             resp = self.lst[self.x_iter][self.y_iter]
#             if self.x_iter == self.y_iter:
#                 self.x_iter += 1
#                 self.y_iter = 0
#             else:
#                 self.y_iter += 1
#             return resp
#         except IndexError:
#             if self.x_iter == len(self.lst):
#                 raise StopIteration
#             else:
#                 raise IndexError("index out of range")

# # task 7

# class IterColumn:

#     def __init__(self, lst, column):
#         self.lst = lst
#         self.x_iter = 0
#         if isinstance(column, int) and 0 <= column < len(lst):
#             self.y_iter = column
#         else:
#             raise IndexError(f'List {self.lst!r} doesn\'t have column {column}')

#     def __iter__(self):
#         self.x_iter = 0
#         return self

#     def __next__(self):
#         try:
#             resp = self.lst[self.x_iter][self.y_iter]
#             self.x_iter += 1
#             return resp
#         except IndexError:
#             if self.x_iter == len(self.lst):
#                 raise StopIteration
#             else:
#                 raise IndexError("index out of range")


# lst = [['x00', 'x01', 'x02'],
#        ['x10', 'x11', 'x12'],
#        ['x20', 'x21', 'x22'],
#        ['x30', 'x31', 'x32']]


# a = IterColumn(lst, 'dd')
# for x in a:
#     print(x)

# b = iter(a)
# print(next(b))



# print('----------------------')
# c = iter(a)
# print(next(c))
# print(next(c))
# print('----------------------')
# print(next(b))
# print(next(b))
# print(next(b))

# # task 8
# class StackObj:

#     def __init__(self, data, _next=None) -> None:
        
#         self.data = data
#         self.next = next

#     @property
#     def data(self):
#         return self.__data

#     @data.setter
#     def data(self, val: any) -> None:
#         self.__data = val

#     @property
#     def next(self):
#         return self.__next

#     @next.setter
#     def next(self, next) -> None:
#         self.__next = next

# class Stack:

#     def __init__(self):
#         self.top = None
#         self.head = None
#         self.lenght = 0
#         self.iter_idx = 0

#     def push_front(self, obj):
#         if self.top is None:
#             self.top = obj
#             self.head = obj
#         else:
#             obj.next = self.head
#             self.head = obj
#         self.lenght += 1

#     def push_back(self, obj):
#         if self.top is None:
#             self.top = obj
#             self.head = obj
#         else:
#             self.top.next = obj
#             self.top = obj
#         self.lenght += 1
    
#     def __len__(self):
#         return self.lenght

#     def __getitem__(self, index):
#         if index < 0 or index > self.lenght - 1:
#             raise IndexError('неверный индекс')
#         resp = self.head
#         for i in range(index):
#             resp = resp.next
#         return resp.data

#     def __setitem__(self, index, value):
#         if index < 0 or index > self.lenght - 1:
#             raise IndexError('неверный индекс')
#         resp = self.head
#         for i in range(index):
#             resp = resp.next
#         resp.data = value

#     def __iter__(self):
#         self.iter_idx = 0
#         return self
    
#     def __next__(self):
#         resp = self.head
#         if self.iter_idx == self.lenght - 1:
#             self.iter_idx = 0
#             raise StopIteration
#         for i in range(self.iter_idx):
#             resp = resp.next
#         self.iter_idx += 1
#         return resp

            
# st = Stack()
# st.push_back(StackObj("1"))
# st.push_front(StackObj("2"))

# assert st[0] == "2" and st[1] == "1", "неверные значения данных из объектов стека, при обращении к ним по индексу"

# st[0] = "0"
# assert st[0] == "0", "получено неверное значение из объекта стека, возможно, некорректно работает присваивание нового значения объекту стека"

# for obj in st:
#     assert isinstance(obj, StackObj), "при переборе стека через цикл должны возвращаться объекты класса StackObj"

# try:
#     a = st[3]
# except IndexError:
#     assert True
# else:
#     assert False, "не сгенерировалось исключение IndexError"