# id, name, price, weight, dims

#  id, name, price, memory, frm
import uuid

class Thing:

    # @staticmethod
    # def _id_gen():
    #     id = 0
    #     while True:
    #         id += 1
    #         yield id

    # _id_gen_inst = _id_gen()

    def __init__(self, name, price, weight=None, dims=None, memory=None, frm=None):

        self.id = hash(self)
        self.name = name
        self.price = price
        self.weight = weight
        self.dims = dims
        self.memory = memory
        self.frm = frm

    def get_data(self):
        return (tuple(self.__dict__.values()))


class Table(Thing):

    def __init__(self, name, price, weight, dims):
        super().__init__(name, price, weight=weight, dims=dims)


class ElBook(Thing):
    
    def __init__(self, name, price, memory, frm):
        super().__init__(name, price, memory=memory, frm=frm)


table = Table("Круглый", 1024, 812.55, (700, 750, 700))
table1 = Table("Круглый", 1024, 812.55, (700, 750, 700))
book = ElBook("Python ООП", 2000, 2048, 'pdf')
book1 = ElBook("Python ООП", 2000, 2048, 'pdf')
print(*table.get_data())
print(*table1.get_data())
print(*book.get_data())
print(*book1.get_data())
