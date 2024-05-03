class Thing:

    def __init__(self, name, price, weight):
        self.name = name
        self.price = price
        self.weight = weight

    def __eq__(self, other):
        return (self.name == other.name
                and self.price == other.price
                and self.weight == other.weight)

    def __hash__(self):
        return hash(self.name) + hash(self.price) + hash(self.weight)


class DictShop(dict):

    def __new__(cls, arg=None):
        if arg is None:
            return super().__new__(cls)
        else:
            if not isinstance(arg, dict):
                raise TypeError('аргумент должен быть словарем')
            for key in arg.keys():
                if not isinstance(key, Thing):
                    raise TypeError('ключами могут быть только объекты класса Thing')
            return super().__new__(cls, arg)

    def __setitem__(self, key: Thing, value: any) -> None:
        if not isinstance(key, Thing):
            raise TypeError('ключами могут быть только объекты класса Thing')
        return super().__setitem__(key, value)


thing1 = Thing(1,2,3)
thing2 = Thing(1,2,4)

a = DictShop()
a[thing1] = 1
a[thing2] = 2
b = DictShop(a)

print(a)
print(b)

th_1 = Thing('Лыжи', 11000, 1978.55)
th_2 = Thing('Книга', 1500, 256)
dict_things = DictShop()
dict_things[th_1] = th_1
dict_things[th_2] = th_2

for x in dict_things:
    print(x.name)

# c = DictShop({'t1': th_1, 't2': th_1})

# print(c)
# dict_things[1] = th_1 # исключение TypeError