class Animal:
    def __init__(self, name, kind, old):
        self.__name = name
        self.__kind = kind
        self.__old = old
    
    @property
    def name(self):
        return self.__name
    
    @name.setter
    def name(self, new_name):
        self.__name = new_name

    @property
    def kind(self):
        return self.__kind
    
    @kind.setter
    def kind(self, new_kind):
        self.__kind = new_kind

    @property
    def old(self):
        return self.__old
    
    @old.setter
    def old(self, new_old):
        self.__old = new_old


animals = [
    Animal("Васька",  "дворовый кот", 5),
    Animal("Рекс", "немецкая овчарка", 8),
    Animal("Кеша", "попугай", 3),
]