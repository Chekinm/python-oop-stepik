# # task 4
# from collections import Counter


# class NewList:

#     def __init__(self, ls=None):
#         if ls is None:
#             self.__list = []
#         else:
#             self.__list = ls.copy()

#     @staticmethod
#     def sub_lists_slow(list1, list2):
#         left = list1.copy()
#         right = list2.copy()
#         left_idx = 0
#         right_idx = 0

#         while left_idx < len(left):
#             if (left[left_idx] != right[right_idx] or
#                     type(left[left_idx]) is not type(right[right_idx])):
#                 right_idx += 1
#                 if right_idx >= len(right):
#                     left_idx += 1
#                     right_idx = 0
#             else:
#                 left.pop_back(left_idx)
#                 right.pop_back(right_idx)
#                 right_idx = 0

#         return left


#     @staticmethod
#     def sub_lists(left, right):
#         res = []
#         right_counter = Counter((elem, type(elem)) for elem in right)

#         for item in left:
#             search_key = (item, type(item))
#             count = right_counter[search_key]
#             if count == 0:
#                 res.append(item)
#             else:
#                 right_counter[search_key] = count - 1
#         return res

#     def __sub__(self, other):

#         if isinstance(other, (NewList, list)):
#             left_op = self.__list
#             right_op = other if isinstance(other, list) else other.get_list()
#             return NewList(self.sub_lists(left_op, right_op))

#         raise NotImplementedError(f'__sub__ is not emplemented between {type(self)} and {type(other)}')

#     def __rsub__(self, other):
#         if isinstance(other, (NewList, list)):

#             left_op = (other if isinstance(other, list) else other.get_list())
#             right_op = self.__list
#             return NewList(self.sub_lists(left_op, right_op))

#         raise NotImplementedError(f'__rsub__ is not emplemented between {type(other)}  and {type(self)}')

#     def __isub__(self, other):

#         if isinstance(other, (NewList, list)):
#             left_op = self.__list
#             right_op = other if isinstance(other, list) else other.get_list()
#             self.__list = self.sub_lists(left_op, right_op).copy()
#             return self

#         raise NotImplementedError(f'__sub__ is not emplemented between {type(self)} and {type(other)}')

#     def get_list(self):
#         return self.__list.copy()



# res = NewList(list(range(1, 100000000))) - list(range(1, 10000000))






# lst = NewList()
# lst1 = NewList([0, 1, -3.4, "abc", True])
# lst2 = NewList([1, 0, True])

# assert lst1.get_list() == [0, 1, -3.4, "abc", True] and lst.get_list() == [], "метод get_list вернул неверный список"

# res1 = lst1 - lst2
# print(res1.get_list())
# res2 = lst1 - [0, True]
# print(res2.get_list())
# res3 = [1, 2, 3, 4.5] - lst2
# print(res3.get_list())
# lst1 -= lst2
# print('4', lst1.get_list())


# assert res1.get_list() == [-3.4, "abc"], "метод get_list вернул неверный список"
# assert res2.get_list() == [1, -3.4, "abc"], "метод get_list вернул неверный список"
# assert res3.get_list() == [2, 3, 4.5], "метод get_list вернул неверный список"
# assert lst1.get_list() == [-3.4, "abc"], "метод get_list вернул неверный список"

# lst_1 = NewList([1, 0, True, False, 5.0, True, 1, True, -7.87])
# lst_2 = NewList([10, True, False, True, 1, 7.87])
# res = lst_1 - lst_2

# assert res.get_list() == [0, 5.0, 1, True, -7.87], "метод get_list вернул неверный список"

# a = NewList([2, 3])
# res_4 = [1, 2, 2, 3] - a # NewList: [1, 2]
# assert res_4.get_list() == [1, 2], "метод get_list вернул неверный список"

# # task 5

# class ListMath:

#     def __init__(self, ls=None):
#         if ls is None:
#             self.lst_math = []
#         else:
#             self.lst_math = list(filter(lambda x: type(x) in (int, float) and type(x) is not bool, ls))

#     def perform(func):
#         func_name = func.__name__
#         if func_name[2] == 'r':
#             def perform_right(self, other):
#                 return ListMath(list(map(lambda x: x.__getattribute__(func_name)(other), self.lst_math)))
#             return perform_right

#         elif func_name[2] == 'i':

#             def perform_self(self, other):
#                 self.list = list(map(lambda x: x.__getattribute__(func_name)(other), self.lst_math))
#             return perform_self
    
#         def perform_left(self, other):
#             return ListMath(list(map(lambda x: x.__getattribute__(func_name)(other), self.lst_math)))
#         return perform_left
    



#     @perform
#     def __add__(self, other):
#         pass

#     @perform
#     def __radd__(self, other):
#         pass


#     @perform
#     def __mul__(self, other):
#         pass

#     @perform
#     def __rmul__(self, other):
#         pass

#     @perform
#     def __truediv__(self, other):
#         pass

#     @perform
#     def __rtruediv__(self, other):
#         pass

#     @perform
#     def __sub__(self, other):
#         pass

#     @perform
#     def __rsub__(self, other):
#         pass


# # task 6

# class StackObj:

#     def __init__(self, data):
#         self.data = data
#         self.next = None

#     @property
#     def data(self):
#         return self.__data

#     @data.setter
#     def data(self, data):
#         self.__data = data

#     @property
#     def next(self):
#         return self.__next

#     @next.setter
#     def next(self, next):
#         self.__next = next

#     def __str__(self):
#         return self.data


# class Stack:

    
#     def __init__(self):
#         self.__top = None
    
#     @property
#     def top(self):
#         return self.__top

#     def push_back(self, obj):
#         obj.next = self.top
#         self.__top = obj

#     def pop_back(self):
#         if self.top:
#             response = self.top
#             self.__top = self.top.next
#             return response
#         else:
#             raise IndexError("Trying to pop_back from epmty stack")
        
#     def __add__(self, other):
#         self.push_back(other)
#         return self
        
    
#     def __iadd__(self, other):
#         self.push_back(other)
#         return self

#     def __mul__(self, other):
#         for obj in other:
#             o = StackObj(obj)
#             self.push_back(o)
#         return self
    
#     def __imul__(self, other):
#         for obj in other:
#             o = StackObj(obj)
#             self.push_back(o)
#         return self

#     def get_data(self):
#         result = []
#         if self.top:
#             counter = self.top
#             while counter:
#                 result.append(counter.data)
#                 counter = counter.next
#         return list(reversed(result))


# # st = Stack()
# # obj1 = StackObj("obj1")
# # st.push_back(obj1)
# # st.push_back(StackObj(12))
# # st.push_back(StackObj([1, 2, 3]))
# # print(st.pop_back().data)
# # st.push_back(StackObj("obj4"))
# # print(st.pop_back().data)
# # st.push_back(StackObj("obj5"))

# # h = st.top
# # print(h.data)
# # while h:
# #     print(h.data, end=' ')
# #     h = h.next
# # else:
# #     print('')
# # st = st + StackObj('added')
# # st = st + StackObj('added1')

# # h = st.pop_back()
# # print(st)
# # while h:
# #     print(h.data, end=' ')
    
# #     h = h.next
# # else:
# #     print('')
# # st += StackObj('selfadded')
# # h = st.top

# # while h:
# #     print(h.data, end=' ')
# #     h = h.next
# # else:
# #     print('')
# # st += StackObj('selfadded')

# # while h:
# #     print(h.data, end=' ')
# #     h = h.next
# # else:
# #     print('')
# # st = st * [StackObj('1'), StackObj('2'), StackObj('3')]
# # st *=  [StackObj('4'), StackObj('5'), StackObj('6')]

# # while h:
    
# #     print(h.data)
# #     h = h.next

# # task 7


# class Book:

#     def __init__(self, title, author, year):
#         self.title = title
#         self.author = author
#         self.year = year


# class Lib:
    
#     def __init__(self) -> None:
#         self.book_list = []

    
#     def __add__(self, other):
#         self.book_list.append(other)
#         return self
    
#     def __iadd__(self, other):
#         self.book_list.append(other)
#         return self
    
#     def __sub__(self, other):
#         if isinstance(other, Book):
#             if other in self.book_list:
#                 self.book_list.remove(other)
#             else:
#                 raise ValueError
#         elif type(other) == int:
#             if other >= 0 and other < len(self.book_list):
#                 self.book_list.pop(other)
#         return self
    
#     def __isub__(self, other):
#         return self.__sub__(other)

#     def __len__(self):
#         return len(self.book_list)

# # task 8

# class Item:

#     def __init__(self, name: str, money: int | float) -> None:
#         self.name = name
#         self.money = money

#     def __add__(self, other_item, *items):
#         res = self.money
#         for item in (other_item, *items):
#             res += item.money
#         return 
    
#     def __radd(self, other):
#         return other + self.money
    

# class Budget:

#     def __init__(self):
#         self.spends = []
    
#     def add_item(self, item):
#         self.spends.append(item)


#     def remove_item(self, idx):
#         if idx >=0 and idx < len(self.spends):
#             self.spends.pop(idx)

#     def get_items(self):
#         return self.spends


# # task 9

# class Box3D:

#     def __init__(self, width, height, depth):
#         self.width = width
#         self.height = height
#         self.depth = depth
    
#     def __add__(self, other):
        
#         return Box3D(self.width + other.width,
#                      self.height + other.height,
#                      self.depth + other.depth,
#                      )
    

#     def __sub__(self, other):
        
#         return Box3D(self.width - other.width,
#                      self.height - other.height,
#                      self.depth - other.depth,
#                      )
    
#     def __mul__(self, number):
        
#         return Box3D(self.width * number,
#                      self.height * number,
#                      self.depth * number,
#                      )
    
#     def __rmul__(self, number):
        
#         return Box3D(self.width * number,
#                      self.height * number,
#                      self.depth * number,
#                      )
    
#     def __floordiv__(self, number):
        
#         return Box3D(self.width // number,
#                      self.height // number,
#                      self.depth // number,
#                      )
    
    
#     def __mod__(self, number):
        
#         return Box3D(self.width % number,
#                      self.height % number,
#                      self.depth % number,
#                      )


# # task 10

# class MaxPooling:

#     def __init__(self, step=(2, 2), size=(2, 2)):
#         self.step = step
#         self.size = size

#     def count_square(self, x, y, matrix):
#         result = 0
#         size_x, size_y = self.size
#         print(size_x, size_y)
        
#         len_x, len_y = len(matrix[0]), len(matrix)

#         if (x + size_x > len_x or 
#                 y + size_y > len_y):
#             print('eee', f'{x=}, {y=},{len_x=},{size_x=}, {len_y=},{size_y=}')
#             raise ValueError("Неверный формат для первого параметра matrix.")

#         for _x in range(x, x + size_x):
#             for _y in range(y, y + size_y):
#                 if isinstance(matrix[_x][_y], (int, float)):
#                     result = max(result, matrix[_x][_y])
#                 else:
#                     print(f'{type(matrix[_x][_y])}')
#                     print('sss', f'{x=}, {y=},{len_x=},{size_x=}')
#                     raise ValueError("Неверный формат для первого параметра matrix.")
#         print(result)
#         return result
    

#     @staticmethod
#     def check_matrix(matrix):

#         if not (isinstance(matrix, list)):
#             raise ValueError("Неверный формат для первого параметра matrix.")
        
#         len_x = len(matrix[0])

#         for row in matrix:
#             if not (isinstance(row, list)) or len(row)!= len_x:
#                 raise ValueError("Неверный формат для первого параметра matrix.")
        
#         return True

        

        


#     def __call__(self, matrix):
        
#         self.check_matrix(matrix)
#         print(matrix)

#         size_x, size_y = self.size
#         step_x, step_y = self.step
#         print(f'{step_x=}, {step_y=}')
#         len_x, len_y = len(matrix[0]), len(matrix)
#         result = []
        
#         for x in range(0, len_x // step_x + 1, step_x):
#             if x + size_x > len_x:
#                 continue
#             result.append([])
#             print(result)
#             for y in range(0, len_y // step_y + 1, step_y):
#                 if y + size_y > len_y:
#                     continue
#                 result[x // step_x].append(self.count_square(x, y, matrix))
#         print('sss', result)
#         return result


# mp = MaxPooling(step=(2, 2), size=(2,2))
# m1 = [[1, 10, 10], [5, 10, 0], [0, 1, 2]]
# m2 = [[1, 10, 10, 12], [5, 10, 0, -5], [0, 1, 2, 300], [40, -100, 0, 54.5]]
# res1 = mp(m1)
# res2 = mp(m2)

# assert res1 == [[10]], "неверный результат операции MaxPooling"
# assert res2 == [[10, 12], [40, 300]], "неверный результат операции MaxPooling"

# mp = MaxPooling(step=(3, 3), size=(2,2))
# m3 = [[1, 12, 14, 12], [5, 10, 0, -5], [0, 1, 2, 300], [40, -100, 0, 54.5]]
# res3 = mp(m3)
# assert res3 == [[12]], "неверный результат операции при MaxPooling(step=(3, 3), size=(2,2))"

# try:
#     res = mp([[1, 2], [3, 4, 5]])
# except ValueError:
#     assert True
# else:
#     assert False, "некорректо отработала проверка (или она отсутствует) на не прямоугольную матрицу"

# try:
#     res = mp([[1, 2], [3, '4']])
# except ValueError:
#     assert True
# else:
#     assert False, "некорректо отработала проверка (или она отсутствует) на не числовые значения в матрице"
 

# mp = MaxPooling(step=(1, 1), size=(5, 5))
# res = mp([[5, 0, 88, 2, 7, 65],
#           [1, 33, 7, 45, 0, 1],
#           [54, 8, 2, 38, 22, 7],
#           [73, 23, 6, 1, 15, 0],
#           [4, 12, 9, 1, 76, 6],
#           [0, 15, 10, 8, 11, 78]])    # [[88, 88], [76, 78]]

# assert res == [[88, 88], [76, 78]], "неверный результат операции MaxPooling(step=(1, 1), size=(5, 5))"
 