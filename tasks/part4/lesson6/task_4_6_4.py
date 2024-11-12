class Digit:

    @staticmethod
    def raise_type_error():
        raise TypeError('значение не соответствует типу объекта')

    def __init__(self, value):
        if not isinstance(value, (float, int)):
            self.raise_type_error()
        self.value = value

    def __repr__(self):
        return str(self.value)


class Integer(Digit):
    def __init__(self, value):
        if not type(value) == int: 
            self.raise_type_error()
        super().__init__(value)


class Float(Digit):
    def __init__(self, value):
        if not isinstance(value, float): 
            self.raise_type_error()
        super().__init__(value)


class Positive(Digit):
    def __init__(self, value):
        if not value >= 0:
            self.raise_type_error()
        super().__init__(value)


class Negative(Digit):
    def __init__(self, value):
        if not value < 0:
            self.raise_type_error()
        super().__init__(value)


class PrimeNumber(Integer, Positive):
    ...


class FloatPositive(Float, Positive):
    ...


digits = [PrimeNumber(3), PrimeNumber(1), PrimeNumber(4), FloatPositive(1.5), FloatPositive(9.2), FloatPositive(6.5),
          FloatPositive(3.5), FloatPositive(8.9)]

a = Integer(1)
print(a)
lst_positive = filter(lambda x: isinstance(x, Positive), digits)

lst_float = filter(lambda x: isinstance(x, Float), digits)

print(list(lst_float), list(lst_positive))
