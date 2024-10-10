class Vector:
    @staticmethod
    def _is_same_dimensions(vector1, vector2):
        return vector1.dimension == vector2.dimension 

    def __init__(self, *args):
        self.coords = [*args]
        self.dimension = len(self.coords)

    def __getitem__(self, idx):
        return self.coords[idx]

    def get_coords(self):
        return tuple(self.coords)

    def __add__(self, other):
        if not self._is_same_dimensions(self, other):
            raise TypeError('размерности векторов не совпадают')
        return Vector(*[self[i] + other[i] for i in range(self.dimension)])

    def __sub__(self, other):
        if not self._is_same_dimensions(self, other):
            raise TypeError('размерности векторов не совпадают')
        return Vector(*[self[i] - other[i] for i in range(self.dimension)])
    
    def __str__(self):
        return ', '.join([f'x{i} = {self[i]}' for i in range(self.dimension)])


class VectorInt(Vector):
    
    @staticmethod
    def _is_coords_int(coords):
        for coord in coords:
            if not isinstance(coord, int):
                return False
        return True

    def __init__(self, *args):
        if not self._is_coords_int(args):
            raise ValueError('координаты должны быть целыми числами')
        super().__init__(*args)

    def __add__(self, other):
        res_coords = super().__add__(other)
        if not self._is_coords_int(res_coords):
            return Vector(*res_coords)
        return VectorInt(*res_coords)
    
    def __sub__(self, other):
        res_coords = super().__sub__(other)
        if not self._is_coords_int(res_coords):
            return Vector(*res_coords)
        return VectorInt(*res_coords)

   




a = Vector(1,2,3)
b = Vector(2,3,4)
c = a + b
d = a - b

a = VectorInt(1,2,3)
# b = VectorInt(2,3,4)
c = a + b
d = a - b
print(c, d, sep='\n')
print(c.__class__)
print(d.__class__)