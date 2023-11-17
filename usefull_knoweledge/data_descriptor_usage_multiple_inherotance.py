from dataclasses import dataclass


class Desc:   # core descruptro class

    def __set_name__(self, owner, name):
        self.name = f'_{owner.__name__}__{name}'

    def __get__(self, instance, owner=None):
        if instance is None: # need this check to work with dataclass
            print('instance is none')
            return  # optioanly can add __init and default value
        return getattr(instance, self.name)

    def __set__(self, instance, value):
        setattr(instance, self.name, value)

    def __delete__(self, insance):
        delattr(insance, self.name)


class TypeRestrictedDesc(Desc):

    TYPE_RESTRICTION = object

    def __set__(self, instance, value):
        print(' ** __set__ form TypeCheck')
        if isinstance(value, self.TYPE_RESTRICTION):
            super().__set__(instance, value)
        else:
            raise TypeError(f'Type error. Accept only {self.TYPE_RESTRICTION}')


class SizeRestrictedDesc(Desc):

    def __init__(self, max_size, min_size=0):
        self.min_size = min_size
        self.max_size = max_size

    def __set__(self, instance, value):
        print(' ** __set__ form Size check')

        if self.min_size <= len(value) <= self.max_size:
            super().__set__(instance, value)
        else:
            raise ValueError(f' Value restriction - {self.min_size=}, {self.max_size=}')


class Positive(Desc):

    def __set__(self, instance, value):
        print(' ** __set__ form Positive')
        if value < 0:

            raise ValueError('Value should be positive')
        super().__set__(instance, value)


class Integer(TypeRestrictedDesc):
    TYPE_RESTRICTION = int


class String(TypeRestrictedDesc):
    TYPE_RESTRICTION = str


class SizedRestrictedString(String, SizeRestrictedDesc):
    pass


class PositiveInteger(Integer, Positive):
    pass


class Test:

    restrcited_string = SizedRestrictedString(min_size=10, max_size=20)
    positive_integer = PositiveInteger()

    def __init__(self, pos_int, string):
        print('run test __init__')
        self.restrcited_string = string
        self.positive_integer = pos_int

    def set_pos_int_around_restriciton(self, value):
        self.__positive_integer = value


test = Test(10, 'sdsdfsdfsdfsdfsdf')

print(test.positive_integer)
print(test.restrcited_string)

test.set_pos_int_around_restriciton(-10)
print(test.positive_integer)
test.positive_integer = 5
print(test.positive_integer)



print('\n'*2)


@dataclass
class TestDataCLass:
    pi: PositiveInteger = PositiveInteger()
    rs_string: SizeRestrictedDesc = SizedRestrictedString(max_size=40, min_size=3)


test = TestDataCLass(134, '6chars')
print(test.__dict__, test.pi, test.rs_string)

del test.pi

print(test.__dict__)
