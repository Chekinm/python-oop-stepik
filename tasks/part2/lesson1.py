# # task 3


# class Clock:
#
#     def __init__(self, tm=0):
#         if self.__check_time(tm):
#             self.__clock = tm
#
#     def set_time(self, tm):
#         if self.__check_time(tm):
#             self.__clock = tm
#
#     def __check_time(self, tm):
#         return (type(tm) in (int, ) and
#                 0 <= tm <= 100000)
#
#     def get_time(self):
#         return self.__clock
#
# clock = Clock(4530)

# # task 4

# class Money:

#     def __init__(self, mn):
#         if self.__check_money(mn):
#             self.__money = mn

#     @classmethod    
#     def __check_money(cls, mn):
#         return type(mn) in (int,) and mn >= 0

#     def set_money(self, mn):
#         if self.__check_money(mn):
#             self.__money = mn

#     def get_money(self):
#         return self.__money

#     def add_money(self, money):
    
#         self.set_money(self.get_money() + money.get_money())
#         # gonna be fun to have it worked like this    
        
        


# mn_1 = Money(10)
# mn_2 = Money(20)
# mn_1.set_money(100)
# mn_2.add_money(mn_1)
# m1 = mn_1.get_money()    # 100
# m2 = mn_2.get_money()    # 120
# print(m1, m2)

# # task 6

# class Book:

#     def __init__(self, author, title, price):
#         self.__author = author
#         self.__title = title
#         self.__price = price

#     def set_title(self, title):
#         self.__title = title

#     def set_author(self, author):
#         self.__author = author          

#     def set_price(self, price):
#         self.__price = price

#     def get_title(self):
#         return self.__title
    
#     def get_author(self):
#         return self.__author
    
#     def get_price(self):
#         return self.__price

# # task 7

# class Line:

#     def __init__(self, *coords) -> None:
#         self.set_coords(*coords)

#     def set_coords(self, x1, y1, x2, y2):
#         self.__x1 = x1
#         self.__y1 = y1
#         self.__x2 = x2
#         self.__y2 = y2

#     def get_coords(self):
#         return self.__x1, self.__y1, self.__x2, self.__y2
#     def draw(self):
#         print(*self.get_coords())

# line = Line(1,2,3,4)
# line.draw()

# # task 8


# class Point:

#     def __init__(self, x, y):
#         self.__x = x
#         self.__y = y

#     def get_coord(self):
#         return self.__x, self.__y

#     def __repr__(self):
#         return f'({self.__x}, {self.__y})'


# class Rectangle:

#     def __init__(self, *args):
#         if len(args) == 2:
#             self.set_coords(*args)
#         else:
#             self.set_coords(Point(args[0], args[1]),
#                             Point(args[2], args[3]),
#                             )

#     def set_coords(self, *points: tuple[Point]) -> None:
#         self.__sp, self.__ep = points

#     def get_coords(self):
#         return self.__sp, self.__ep

#     def draw(self):
#         print('Прямоугольник c координатами:', *self.get_coords())


# rect = Rectangle(Point(0, 0), Point(20, 34))

# task 9 

class ObjList:
    def __init__(self, data, prevobj=None, nextobj=None):
        self.set_next(nextobj)
        self.set_prev(prevobj)
        self.set_data(data)

    def set_next(self, obj):
        self.__next = obj
    
    def set_prev(self, obj):
        self.__prev = obj

    def set_data(self, data):
        self.__data = data

    def get_next(self):
        return self.__next
    
    def get_prev(self):
        return self.__prev

    def get_data(self):
        return self.__data

    # def __repr__(self):
    #     return f'{self.get_data()}, prev- {self.get_prev()}, next - {self.get_next()}'

class LinkedList:

    def __init__(self, head: ObjList = None, tail: ObjList = None) -> None:
        self.head = head
        self.tail = tail

    def add_obj(self, obj):
        if self.tail:
            obj.set_prev(self.tail)
            self.tail.set_next(obj)
            self.tail = obj
        else:
            self.head = self.tail = obj

    def remove_obj(self):
        if self.tail:
            self.tail = self.tail.get_prev()
            if self.tail:
                self.tail.set_next(None)
            else:
                self.head = None
        


    def get_data(self):
        current_head = self.head
        data_list = []
        while current_head:
            data_list.append(current_head.get_data())   
            current_head = current_head.get_next()
        return data_list


lst = LinkedList()
obj1 = ObjList("данные 1")
print(obj1)
lst.add_obj(obj1)
print(lst.get_data(), lst.head, lst.tail)

obj2 = ObjList("данные 2")
print(obj2)
lst.add_obj(obj2)
print(lst.get_data(), lst.head, lst.tail)



lst.add_obj(ObjList("данные 3"))
res = lst.get_data()  
print(res)

lst.remove_obj()

res = lst.get_data()  
print(res)

lst.remove_obj()

res = lst.get_data()  
print(res)

lst.remove_obj()

res = lst.get_data()  
print(res)