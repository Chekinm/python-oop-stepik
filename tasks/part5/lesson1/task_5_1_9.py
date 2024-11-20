class Triangle:

    @staticmethod
    def _check_input(*args):
        a, b, c = args
        for arg in args:
            if not isinstance(arg, (int, float)) or arg <= 0:
                raise TypeError('стороны треугольника должны быть положительными числами')
        if a >= b + c or b >= a + c or c >= a + b:
            raise ValueError('из указанных длин сторон нельзя составить треугольник')

    def __new__(cls, *args):
        try:
            cls._check_input(*args)
            return super().__new__(cls)
        except (TypeError, ValueError) as error:
            raise error

    def __init__(self, a, b, c):
        self._a = a
        self._b = b
        self._c = c


def create_triangle(*args):
    try:
        tr = Triangle(*args)
        return tr
    except (ValueError, TypeError):
        return None


input_data = [(1.0, 4.54, 3), ('abc', 1, 2, 3), (-3, 3, 5.2), (4.2, 5.7, 8.7), (True, 3, 5), (7, 4, 6)]

lst_tr = [create_triangle(*sides) for sides in input_data if create_triangle(*sides) is not None]

print(lst_tr)
