class ItemAttrs:
    def __getitem__(self, index):
        # Получаем список всех локальных атрибутов объекта
        attrs = list(self.__dict__.values())
        if 0 <= index < len(attrs):
            return attrs[index]
        raise IndexError("Index out of range")
    
    def __setitem__(self, index, value):
        # Получаем список имен локальных атрибутов
        attrs = list(self.__dict__.keys())
        if 0 <= index < len(attrs):
            # Устанавливаем новое значение атрибута по его имени
            setattr(self, attrs[index], value)
        else:
            raise IndexError("Index out of range")

class Point(ItemAttrs):
    def __init__(self, x, y):
        self.x = x
        self.y = y

pt = Point(1,2)
print(pt[1])
pt.z = 12
print(pt.__dict__)
print(pt[2])