class SellItem:

    def __init__(self, name, price) -> None:
        self.name = name
        self.price = price
    

class House(SellItem):

    def __init__(self, name, price, material, square) -> None:
        super().__init__(name, price)
        self.material = material
        self.square = square


class Flat(SellItem):

    def __init__(self, name, price, size, room) -> None:
        super().__init__(name, price)
        self.size = size
        self.room = room


class Land(SellItem):

    def __init__(self, name, price, square) -> None:
        super().__init__(name, price)
        self.square = square


class Agency:

    def __init__(self, name):
        self.name = name
        self.objects = []

    def get_objects(self):
        return self.objects

    def add_object(self, obj: House | Flat | Land) -> None:
        self.objects.append(obj)

    def remove_object(self, obj: House | Flat | Land) -> None:
        self.objects = filter(lambda x: x.name != obj.name, self.objects)

