class Furniture:
    
    @staticmethod
    def __verify_name(name):
        if not isinstance(name, str):
            raise TypeError('название должно быть строкой')

    @staticmethod
    def __verify_weight(weight):
        if not isinstance(weight, (float, int)) or weight <= 0:
            raise TypeError('вес должен быть положительным числом')


    def __init__(self, name, weight):
        self.__verify_name(name)
        self.__verify_weight(weight)
        self._name = name
        self._weight = weight

    @property
    def name(self):
        return self._name
    
    @name.setter
    def name(self, name):
        self._name = name

    @property
    def weight(self):
        return self._weight
    
    @weight.setter
    def weight(self, weight):
        self._weight = weight

    def get_attrs(self):
        return tuple(value for key, value in self.__dict__.items() if key.startswith("_"))


class Closet(Furniture):

    def __init__(self, name, weight, tp, doors):
        super().__init__(name, weight)
        self._tp = tp
        self._doors = doors


class Table(Furniture):

    def __init__(self, name, weight, height, square):
        super().__init__(name, weight)
        self._height = height
        self._square = square

class Chair(Furniture):

    def __init__(self, name, weight, height):
        super().__init__(name, weight)
        self._height = height
        
cl = Closet('шкаф-купе', 342.56, True, 3)
chair = Chair('стул', 14, 55.6)
tb = Table('стол', 34.5, 75, 10)
print(tb.get_attrs())
