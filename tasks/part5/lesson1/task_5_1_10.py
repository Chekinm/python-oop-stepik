class Validator:

    def __init__(self, min_value, max_value, validation_type):
        self.min_value = min_value
        self.max_value = max_value
        self.validation_type = validation_type

    def __call__(self, value):
        if type(value) != self.validation_type or not (self.min_value <= value <= self.max_value):
            raise ValueError('значение не прошло валидацию')


class FloatValidator(Validator):
    validation_type = float

    def __init__(self, min_value, max_value):
        super().__init__(min_value, max_value, self.validation_type)
        

class IntegerValidator(Validator):
    validation_type = int

    def __init__(self, min_value, max_value):
        super().__init__(min_value, max_value, self.validation_type)


def is_valid(value_arr: list, validators: list[Validator]):
    res_lst = []
    for value in value_arr:
        for validator in validators:
            try: 
                validator(value)
                res_lst.append(value)
                continue
            except ValueError:
                pass
    return res_lst

fv = FloatValidator(0, 10.5)
iv = IntegerValidator(-10, 20)
lst_out = is_valid([1, 4.5, -10.5, 100, True, 'abc', (1, 2)], validators=[fv, iv])   # [1, 4.5]
print(lst_out)