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

# task 6

class StackObj:

    def __init__(self, data):
        self.data = data
        self.next = None

    @property
    def data(self):
        return self.__data

    @data.setter
    def data(self, data):
        self.__data = data

    @property
    def next(self):
        return self.__next

    @next.setter
    def next(self, next):
        if isinstance(next, StackObj) or next is None:
            self.__next = next


class Stack:

    def __init__(self):
        self.__top = None # тот top, который какой надо top
        self.__bottom = None # top курильщика, bottom здорового целовека  
                             

    @property
    def head(self):  # top заняли, назовем head
        return self.__top
    
    @property
    def top(self): # а это - top курильщика, bottom здорового целовека
        return self.__bottom  # хоть горшком назови только в печь не сатвь


    def push(self, obj):
        if self.head is None:    # костыль детектед,
            self.__bottom = obj  # но желание заказчика закон
        obj.next = self.head
        self.__top = obj

    def pop(self):
        if self.head:
            response = self.head
            self.__top = self.head.next
            if self.__top is None:    # костыль не приходит один, если дошли до дна
                self.__bottom = None  # то надо дно (АКА top) обнулить.
            response.next = None
            
            return response
        else:
            raise IndexError("Triing to pop from epmty stack")
    
    def get_data(self):
        result = []
        if self.head:
            counter = self.head
            while counter:
                result.append(counter.data)
                counter = counter.next
        return list(reversed(result))
        
st = Stack()
st.push(StackObj("obj1"))
st.push(StackObj("obj2"))
st.push(StackObj("obj3"))
st.push(StackObj("obj4"))
st.pop()
st.push(StackObj("obj5"))


res = st.get_data() 
print(res)
