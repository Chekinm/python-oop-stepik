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

