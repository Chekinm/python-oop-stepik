class Rect:
    @staticmethod
    def _input_check(*args):
        x, y, width, height = args
        try:
            res = map(float, args)
        except:
            raise ValueError('некорректные координаты и параметры прямоугольника')
        else:
            if width <= 0 or height <= 0:
                raise ValueError('некорректные координаты и параметры прямоугольника')

    @staticmethod
    def _is_not_inteval_intersect(interval_1, interval_2):
        x1, len1 = interval_1
        x2, len2 = interval_2
        if x1 <= x2:
            return x1 + len1 < x2
        else:
            return x2 + len2 < x1



    def __init__(self, x, y, width, height) -> None:
        self._input_check(x, y, width, height)
        self._x = x
        self._y = y
        self._width = width
        self._height = height

    def __repr__(self):
        return f'x={self._x}, y={self._y}, w={self._width}, h={self._height}'

    def is_collision(self, rect):
        if (self._is_not_inteval_intersect((self._x, self._width), (rect._x, rect._width)) or
            self._is_not_inteval_intersect((self._y, self._height), (rect._y, rect._height))):
            pass
        else:
            raise TypeError('прямоугольники пересекаются')

lst_rect = [Rect(0, 0, 5, 3), Rect(6, 0, 3, 5), Rect(3, 2, 4, 4), Rect(0, 8, 8, 1)]
lst_not_collision = []
for r in lst_rect:
    try:
        for other in lst_rect:
            if r != other:                
                r.is_collision(other)
    except:
        continue
    else:
        lst_not_collision.append(r)
