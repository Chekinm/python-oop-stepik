class Animal:

    def __init__(self, name, old):
        self.name = name
        self.old = old


class Cat(Animal):

    def __init__(self, name, old, color, weight):
        self.color = color
        self.weight = weight
        super().__init__(name, old)

    def get_info(self):
        return f'{self.name}: {self.old}, {self.color}, {self.weight}'

class Dog(Animal):

    def __init__(self, name, old, breed, size):
        self.breed = color
        self.size = weight
        super().__init__(name, old)

    def get_info(self):
        return f'{self.name}: {self.old}, {self.breed}, {self.size}'


a = Cat('m', 4, 'brown', 50)
print(a.__dict__)
