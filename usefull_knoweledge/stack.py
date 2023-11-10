class Stack:

    class _StackObj:

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
            self.__next = next

        def __str__(self):
            return self.data

    @classmethod
    def __to_StackObj(cls, data):
        return cls._StackObj(data)

    def __init__(self):
        self.__head = None

    @property
    def head(self):
        return self.__head

    def push(self, data):
        obj = self.__to_StackObj(data)
        obj.next = self.head
        self.__head = obj

    def pop(self):
        if self.head:
            response = self.head.data
            self.__head = self.head.next
            return response
        else:
            raise IndexError("Trying to pop from epmty stack")
    
    def get_data(self):
        result = []
        if self.head:
            counter = self.head
            while counter:
                result.append(counter.data)
                counter = counter.next
        return list(reversed(result))


st = Stack()
st.push("obj1")
st.push(12)
st.push([1, 2, 3])
print(st.pop())
st.push("obj4")
print(st.pop())
st.push("obj5")


res = st.get_data() 
print(res)
