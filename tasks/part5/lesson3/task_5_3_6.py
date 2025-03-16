class TupleLimit(tuple):

    def __new__(cls, lst, max_lenght):
        if len(lst) > max_lenght:
            raise ValueError('число элементов коллекции превышает заданный предел')
        return super().__new__(cls, lst)

    def __init__(self, lst, max_lenght):
        self.max_lenght = max_lenght

    def __str__(self):
        return ' '.join(map(str, self))

    def __repr__(self):
        return ' '.join(map(str, self))

digits = [1,2,3,4,5,6]
try:
    tp = TupleLimit(digits, 5)
    print(tp)
except ValueError as e:
    print(e)