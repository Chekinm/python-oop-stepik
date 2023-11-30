class A:
    def __init__(self, value):
        self.value = value

    # def __str__(self):
    #     print('_str')

    #     return f'{self.value=}'
    def __repr__(self):
        print('_repr')
        return f'{self.value=}'

a = A(5)
b = A(4)
c = [a, b]
print(c)
print(a)
s = str(a)
print(s)
a += 234.0