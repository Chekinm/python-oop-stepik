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
#                 left.pop(left_idx)
#                 right.pop(right_idx)
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

# task 5

class ListMath:

    def __init__(self, ls=None):
        if ls is None:
            self.lst_math = []
        else:
            self.lst_math = list(filter(lambda x: type(x) in (int, float) and type(x) is not bool, ls))

    def perform(func):
        func_name = func.__name__
        if func_name[2] == 'r':
            def perform_right(self, other):
                return ListMath(list(map(lambda x: x.__getattribute__(func_name)(other), self.lst_math)))
            return perform_right

        elif func_name[2] == 'i':

            def perform_self(self, other):
                self.list = list(map(lambda x: x.__getattribute__(func_name)(other), self.lst_math))
            return perform_self
    
        def perform_left(self, other):
            return ListMath(list(map(lambda x: x.__getattribute__(func_name)(other), self.lst_math)))
        return perform_left
    



    @perform
    def __add__(self, other):
        pass

    @perform
    def __radd__(self, other):
        pass


    @perform
    def __mul__(self, other):
        pass

    @perform
    def __rmul__(self, other):
        pass

    @perform
    def __truediv__(self, other):
        pass

    @perform
    def __rtruediv__(self, other):
        pass

    @perform
    def __sub__(self, other):
        pass

    @perform
    def __rsub__(self, other):
        pass





        




lst1 = ListMath()
lp = [1, False, 2, -5, "abc", 7]
lst2 = ListMath(lp)
lst3 = ListMath(lp)

assert id(lst2.lst_math) != id(lst3.lst_math), "внутри объектов класса ListMath должна создаваться копия списка"

assert lst1.lst_math == [] and lst2.lst_math == [1, 2, -5, 7], "неверные значения в списке объекта класса ListMath"

res1 = lst2 + 76
lst = ListMath([1, 2, 3])
lst += 5
assert lst.lst_math == [6, 7, 8] and res1.lst_math == [77, 78, 71, 83], "неверные значения, полученные при операциях сложения"

lst = ListMath([0, 1, 2])
res3 = lst - 76
res4 = 7 - lst
assert res3.lst_math == [-76, -75, -74] and res4.lst_math == [7, 6, 5], "неверные значения, полученные при операциях вычитания"

lst -= 3
assert lst.lst_math == [-3, -2, -1], "неверные значения, полученные при операции вычитания -="

lst = ListMath([1, 2, 3])
res5 = lst * 5
res6 = 3 * lst
lst *= 4
assert res5.lst_math == [5, 10, 15] and res6.lst_math == [3, 6, 9], "неверные значения, полученные при операциях умножения"
assert lst.lst_math == [4, 8, 12], "неверные значения, полученные при операциях умножения"

lst = lst / 2
lst /= 13.0
