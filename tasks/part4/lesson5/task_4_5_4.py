class ShopInterface:

    def get_id(self):
        raise NotImplementedError('в классе не переопределен метод get_id')
    

class ShopItem(ShopInterface):
    items_counter = 0
    @classmethod
    def create_new_id(cls):
        cls.items_counter += 1
        return cls.items_counter

    def __init__(self, name, weight, price):
        self._name = name
        self._weight = weight
        self._price = price
        self.__id = self.create_new_id()
    
    def get_id(self):
        return self.__id