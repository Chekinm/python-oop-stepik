class Point:
    def __init__(self, x=0, y=0):
        self._x = x
        self._y = y

    def __str__(self):
        return f'Point: x = {self._x}, y = {self._y}'


x, y = input().split()

try:
    x = int(x)
    y = int(y)
    pt = Point(x, y)
except:
    try:
        x = float(x)
        y = float(y)
        pt = Point(x, y)
    except:
        pt = Point()

finally:
    print(pt)