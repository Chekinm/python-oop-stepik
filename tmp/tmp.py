# def s(*items):
#     if len(items):
#         res = items[0]
#         for item in items[1:]:
#             try:
#                 res += item
#             except TypeError:
#                 continue
#         return res
#     return None
#
# print(s(1, 'd', 's', 3))
#
# def move_zeros_to_end(arr):
#     zeros = 1
#     i = 0
#     while i + zeros < len(arr) - 1:
#         if arr[i] == 0:
#             arr[i], arr[i+zeros] = arr[i+zeros], arr[i]
#             if arr[i] == 0:
#                 zeros += 1
#         else:
#             i += 1
#     return arr
#
#
#
# a = [0 , 1, 2,3,4,0,6,7,0]
# print(a)
# print(move_zeros_to_end(a))
#

from dataclasses import dataclass

@dataclass
class Data:
    data: str
    ip: int

Data('sdf', 20)

