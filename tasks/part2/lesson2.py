# # task 4

# class Car:
#     def __init__(self, model):
#         self.model = model

#     @property
#     def model(self):
#         return self.__model

#     @model.setter
#     def model(self, model):
#         if isinstance(model, str) and 2 <= len(model) <= 100:
#             self.__model = model

# c = Car('sdf')
# print(c.model, c.__dict__)
# c.model = "Toyp"
# print(c.model, c.__dict__)
# c.model = 1
# print(c.model, c.__dict__)
# c.model = 'ferrari'
# print(c.model, c.__dict__)

# # task 5

# class WindowDlg:
#     SIZE_MIN = 0
#     SIZE_MAX = 10000
#     def __init__(self, title: str, width: int, height: int) -> None:
#         self.__title = title
#         self.__width = width
#         self.__height = height

#     def show(self):
#         print(f'{self.title}: {self.width}, {self.height}')
    
#     @classmethod
#     def check_size(cls, size):
#         return type(size) == int and cls.SIZE_MIN <= size <= cls.SIZE_MAX

#     @property
#     def title(self):
#         return self.__title
    
#     @title.setter
#     def title(self, title):
#         if isinstance(title, str):
#             self.__title = title

#     @property
#     def width(self):
#         return self.__width
    
#     @width.setter
#     def width(self, width):
#         if self.check_size(width):
#             self.__width = width
#             self.show()

#     @property
#     def height(self):
#         return self.__height
    
#     @height.setter
#     def height(self, height):
#         if self.check_size(height):
#             self.__height = height
#             self.show()

# a = WindowDlg('d', 1, 2)
# a.width = True
# a.height = False

# a.width = 100000
# a.height = 100000
# a.show()

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
#         if isinstance(next, StackObj) or next is None:
#             self.__next = next


# class Stack:

#     def __init__(self):
#         self.__top = None # тот top, который какой надо top
#         self.__bottom = None # top курильщика, bottom здорового целовека  
                             

#     @property
#     def head(self):  # top заняли, назовем head
#         return self.__top
    
#     @property
#     def top(self): # а это - top курильщика, bottom здорового целовека
#         return self.__bottom  # хоть горшком назови только в печь не сатвь


#     def push(self, obj):
#         if self.head is None:    # костыль детектед,
#             self.__bottom = obj  # но желание заказчика закон
#         obj.next = self.head
#         self.__top = obj

#     def pop(self):
#         if self.head:
#             response = self.head
#             self.__top = self.head.next
#             if self.__top is None:    # костыль не приходит один, если дошли до дна
#                 self.__bottom = None  # то надо дно (АКА top) обнулить.
#             response.next = None
            
#             return response
#         else:
#             raise IndexError("Triing to pop from epmty stack")
    
#     def get_data(self):
#         result = []
#         if self.head:
#             counter = self.head
#             while counter:
#                 result.append(counter.data)
#                 counter = counter.next
#         return list(reversed(result))
        
# st = Stack()
# st.push(StackObj("obj1"))
# st.push(StackObj("obj2"))
# st.push(StackObj("obj3"))
# st.push(StackObj("obj4"))
# st.pop()
# st.push(StackObj("obj5"))


# res = st.get_data() 
# print(res)

# task 

# # task 7

# class RadiusVector2D:
#     MIN_COORD = -100
#     MAX_COORD = 1024

#     @classmethod
#     def _check_coord(cls, num):
#         return (isinstance(num, (int, float)) and
#                 cls.MIN_COORD <= num <= cls.MAX_COORD)

#     def __init__(self, x=0, y=0):
#         self.__x = x if self._check_coord(x) else 0
#         self.__y = y if self._check_coord(x) else 0
    
#     @property
#     def x(self):
#         return self.__x
    
#     @x.setter
#     def x(self, x):
#         if self._check_coord(x):
#             self.__x = x

#     @property
#     def y(self):
#         return self.__y
    
#     @y.setter
#     def y(self, y):
#         if self._check_coord(y):
#             self.__y = y

#     @staticmethod
#     def norm2(vector):
#         return vector.x ** 2 + vector.y ** 2
    
#     def __str__(self):
#         return f'x: {self.x}, y: {self.y}' 

# r1 = RadiusVector2D()
# r2 = RadiusVector2D(1)
# r3 = RadiusVector2D(4, 5)

# assert hasattr(RadiusVector2D, 'MIN_COORD') and hasattr(RadiusVector2D, 'MAX_COORD'), "в классе RadiusVector2D должны присутствовать атрибуты MIN_COORD и MAX_COORD"

# assert type(RadiusVector2D.x) == property and type(RadiusVector2D.y) == property, "в классе RadiusVector2D должны присутствовать объекты-свойства x и y"

# assert r1.x == 0 
# assert r1.y == 0 
# assert r2.x == 1 
# assert r2.y == 0 
# assert r3.x == 4 
# assert r3.y == 5

# assert RadiusVector2D.norm2(r3) == 41, "неверно вычисляется норма вектора"

# r4 = RadiusVector2D(4.5, 5.5)
# assert 4.4 < r4.x < 4.6 and 5.4 < r4.y < 5.6, "свойства x и y возвращают неверные значения"

# r5 = RadiusVector2D(-102, 2000)
# assert r5.x == 0 and r5.y == 0, "присвоение значений, выходящих за диапазон [-100; 1024] не должно выполняться"

# r = RadiusVector2D(10, 20)
# r.x = 'a'
# r.y = (1, 2)
# assert r.x == 10 and r.y == 20, "присвоение не числовых значений должно игнорироваться"

# task 8 

# class TreeObj:

#     def __init__(self, index, value=None):
#         self.__index = index
#         self.__value = value
#         self.left = None
#         self.right = None

#     @property
#     def index(self):
#         return self.__index

#     @property
#     def value(self):
#         return self.__value

#     @property
#     def left(self):
#         return self.__left

#     @left.setter
#     def left(self, left):
#         self.__left = left

#     @property
#     def right(self):
#         return self.__right

#     @right.setter
#     def right(self, right):
#         self.__right = right
    
#     def __str__(self):
#         return self.value

# class DecisionTree:

#     def __new__(cls):
#         return None
    
#     @classmethod
#     def add_obj(cls, obj, node=None, left=True):
#         if node:
#             if left:
#                 node.left = obj
#             else:
#                 node.right = obj
#         return obj
    
#     @classmethod
#     def predict(cls, root, x):
#         try:
#             current_node = root
#             while current_node:
#                 result = current_node.value
#                 if x[current_node.index]:
#                     current_node = current_node.left
#                 else:
#                     current_node = current_node.right
#             return result
#         except IndexError:
#             return None

# root = DecisionTree.add_obj(TreeObj(0))
# v_11 = DecisionTree.add_obj(TreeObj(1), root)
# v_12 = DecisionTree.add_obj(TreeObj(2), root, False)
# DecisionTree.add_obj(TreeObj(-1, "будет программистом"), v_11)
# DecisionTree.add_obj(TreeObj(-1, "будет кодером"), v_11, False)
# DecisionTree.add_obj(TreeObj(-1, "не все потеряно"), v_12)
# DecisionTree.add_obj(TreeObj(-1, "безнадежен"), v_12, False)

# x = [1, 1, 0]
# res = DecisionTree.predict(root, x) # будет программистом
# print(res)

# # task 9

# from math import sqrt

# class PathLines:
    
#     def __init__(self, *lines):
#         self.lines = list(lines)
#         self.start_x = 0
#         self.start_y = 0

#     def get_path(self):
#         return self.lines
    
#     def add_line(self, line):
#         self.lines.append(line)

#     def get_length(self):
#         length = 0
#         curr_x, curr_y = self.start_x, self.start_y

#         for line in self.lines:
#             segment_lenght = sqrt(
#                 (line.x - curr_x) ** 2 + (line.y - curr_y) ** 2
#                 )
#             length += segment_lenght
#             curr_x, curr_y = line.x, line.y

#         return length


# class LineTo:

#     def __init__(self, x, y):
#         self.x = x
#         self.y = y

# p = PathLines(LineTo(10, 20), LineTo(10, 30))
# p.add_line(LineTo(20, -10))
# dist = p.get_length()
# print(dist)

# task 10

# class PhoneBook:

#     def __init__(self):
#         self.phone_list = []

#     def add_phone(self, phone):
#         self.phone_list.append(phone)

#     def remove_phone(self, index):
#         self.phone_list.pop(index)
        
#     def get_phone_list(self):
#         return self.phone_list


# class PhoneNumber:

#     def __init__(self, number, fio):
#         self.number = number
#         self.fio = fio

#     def __repr__(self):
#         return f'{self.fio}: {self.number}'

