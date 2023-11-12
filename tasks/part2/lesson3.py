# # task 6

# class FloatValue():

#     def __set_name__(self, owner, name):
#         self.name = '_' + name

#     def __get__(self, instance, owner):
#         return getattr(instance, self.name)

#     def __set__(self, instance, value):
#         if isinstance(value, float):
#             setattr(instance, self.name, value)
#         else:
#             raise TypeError("Присваивать можно только вещественный тип данных.")

# class Cell:
#     value = FloatValue()

#     def __init__(self, value):
#         self.value = value

#     def __repr__(self):
#         return f'{self.value}'


# class TableSheet:

#     def __init__(self, N, M):
#         self.cells = [[Cell(0.0) for _ in range(N)] for _ in range(M)]


# N = 3
# M = 5
# table = TableSheet(N, M)

# for i in range(15):
#     table.cells[i//N][i%N].value = i / 1 + 1

# print(table.cells)

# # task 7

# class ValidateString:

#     def __init__(self, min_length=3, max_length=100):
#         self.min_lenght = min_length
#         self.max_lenght = max_length

#     def validate(self, string):
#         return (isinstance(string, str) and
#                 self.min_lenght <= len(string) <= self.max_lenght
#                 )


# class StringValue:

#     def __init__(self, validator=ValidateString()):
#         self.valildator = validator


#     def __set_name__(self, owner, name):
#         self.name = '_' + name


#     def __get__(self, instance, owner):
#         return getattr(instance, self.name)
    
#     def __set__(self, instance, value):
#         if self.valildator.validate(value):
#             setattr(instance, self.name, value)
            

# class RegisterForm:
#     login = StringValue()
#     password = StringValue()
#     email = StringValue()

#     def __init__(self, login='login', password ='password', email='email'):
#         self.login = login
#         self.password = password
#         self.email = email

#     def get_fields(self):
#         return list(self.__dict__.values())
    
#     def show(self):
#         return f'''<form>\nЛогин: {self.login}\nПароль: {self.password}\nEmail: {self.email}\n</form>'''
        



# c = RegisterForm()

# print(c.get_fields())
# print(c.show())

# print(c.login)

# # task 8

# class StringValue:

#     def __init__(self, min_lenght=2, max_lenght=50):
#         self.__max_lenght = max_lenght
#         self.__min_lenght = min_lenght

#     def __set_name__(self, owner, name):
#         self.name = "_" + name

#     def __get__(self, instance, owner):
#         return getattr(instance, self.name)

#     def __set__(self, instance, value):
#         if (isinstance(value, str) and
#                 self.__min_lenght <= len(value) <= self.__max_lenght):
#             return setattr(instance, self.name, value)


# class PriceValue:

#     def __init__(self, max_value=10000):
#         self.__max_value = max_value

#     def __set_name__(self, owner, name):
#         self.name = "_" + name

#     def __get__(self, instance, owner):
#         return getattr(instance, self.name)

#     def __set__(self, instance, value):
#         if (isinstance(value, int) and 0 <= value <= self.__max_value):
#             return setattr(instance, self.name, value)


# class Product:

#     name = StringValue(min_lenght=2, max_lenght=50)
#     price = PriceValue(max_value=10000)

#     def __init__(self, name, price):
#         self.name = name
#         self.price = price

    
# class SuperShop:

#     def __init__(self, name):
#         self.name = name
#         self.goods = []

#     def add_product(self, product):
#         self.goods.append(product)

#     def remove_product(self, product):
#         if product in self.goods:
#             self.goods.remove(product)
#         else:
#             raise ValueError('Cannot delete unexistent product')


# shop = SuperShop("У Балакирева")
# shop.add_product(Product("Курс по Python", 0))
# shop.add_product(Product("Курс по Python ООП", 2000))
# for p in shop.goods:
#     print(f"{p.name}: {p.price}")

# # task 9


# class Thing:

#     def __init__(self, name, weight):
#         self.name = name
#         self.weight = weight


# class Bag:

#     def __init__(self, max_weight):
#         self.max_weight = max_weight
#         self.__things = []
#         self.__current_weight = 0

#     @property
#     def things(self):
#         return self.__things

#     def add_thing(self, thing):
#         if thing.weight + self.__current_weight <= self.max_weight:
#             self.__current_weight += thing.weight
#             self.__things.append(thing)

#     def remove_thing(self, idx):
#         try:
#             thing = self.__things[idx]
#             self.__things.pop(idx)
#             self.__current_weight -= thing.weight
#         except IndexError:
#             print('trying to remove unexistent things')

#     def get_total_weight(self):
#         return self.__current_weight
    

# bag = Bag(1000)
# bag.add_thing(Thing("Книга по Python", 100))
# bag.add_thing(Thing("Котелок", 500))
# bag.add_thing(Thing("Спички", 20))
# bag.add_thing(Thing("Бумага", 100))
# w = bag.get_total_weight()
# for t in bag.things:
#     print(f"{t.name}: {t.weight}")

# task 10

class TVProgram:

    def __init__(self, chanell_name):
        self.chanell_name = chanell_name
        self.items = []
        self.__dict_items = dict()

    def add_telecast(self, telecast):
        self.__dict_items.setdefault(telecast.uid, telecast)
        self.items = list(self.__dict_items.values())

    def remove_telecast(self, telecastid):
        try:
            self.__dict_items.pop(telecastid, None)

            self.items = list(self.__dict_items.values())
        except IndexError:
            print('tlecast doens\'t exist')


class Telecast:

    def __init__(self, id, name, duration):
        self.uid = id
        self.name = name
        self.duration = duration

    @property
    def uid(self):
        return self.__id

    @uid.setter
    def uid(self, id):
        self.__id = id

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, name):
        self.__name = name

    @property
    def duration(self):
        return self.__duration

    @duration.setter
    def duration(self, duration):
        self.__duration = duration


pr = TVProgram("Первый канал")
pr.add_telecast(Telecast(1, "Доброе утро", 10000))
pr.add_telecast(Telecast(2, "Новости", 2000))
pr.add_telecast(Telecast(3, "Интервью с Балакиревым", 20))
for t in pr.items:
    print(f"{t.name}: {t.duration}")