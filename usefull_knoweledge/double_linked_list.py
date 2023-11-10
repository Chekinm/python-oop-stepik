class LinkedList:

    class __ObjList:
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

        def __repr__(self):
            return f'{self.get_data()}'

    @classmethod
    def __to_objlist(cls, obj):
        return cls.__ObjList(obj)

    def __init__(self) -> None:
        self.head = None
        self.tail = None

    def push_right(self, obj):
        obj = self.__to_objlist(obj)
        if self.tail:
            obj.set_prev(self.tail)
            self.tail.set_next(obj)
            self.tail = obj
        else:
            self.head = self.tail = obj

    def push_left(self, obj):
        obj = self.__to_objlist(obj)
        if self.head:
            obj.set_next(self.head)
            self.head.set_prev(obj)
            self.head = obj
        else:
            self.head = self.tail = obj

    def pop_right(self):
        if self.tail:
            self.tail = self.tail.get_prev()
            if self.tail:
                self.tail.set_next(None)
            else:
                self.head = None
        else:
            raise IndexError("trying to pop from empty list")

    def pop_left(self):
        if self.head:
            self.head = self.head.get_next()
            if self.head:
                self.head.set_prev(None)
            else:
                self.tail = None
        else:
            raise IndexError("trying to pop from empty list")

    def get_data(self):
        current_head = self.head
        data_list = []
        while current_head:
            data_list.append(current_head.get_data())   
            current_head = current_head.get_next()
        return data_list

    def __str__(self):
        return ','.join(map(str, self.get_data()))


lst = LinkedList()
lst.push_right(1)
lst.push_right('strr')
lst.push_right([1, 2, 3])
print(lst)
lst.push_left(11)
lst.push_left(22)
lst.push_left(33)
print(lst)
lst.pop_right()
print(lst)
lst.pop_left()
print(lst)

try:
    lst.pop_left()
    print(lst)
    lst.pop_left()
    print(lst)
    lst.pop_left()
    print(lst)
    lst.pop_left()
    print(lst)
    lst.pop_left()
    print(lst)
except IndexError:
    print('Has trtied to pop for emtpy list')
