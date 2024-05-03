class Tuple(tuple):

    def __new__(cls, content=None):
        if content is None:
            return super().__new__(cls)
        return super().__new__(cls, content)

    def __add__(self, other):
        try:
            new_tuple = tuple([_ for _ in other])
            return Tuple(super().__add__(new_tuple))
        except TypeError:
            raise TypeError("Second operand is not itrable")

a = Tuple((1,2,3))
b= 'ssdsd'

print(a + b)
