# task 4
# class Rect:

#     def __init__(self, x, y, weight, height):
#         self.x = x
#         self.y = y
#         self.weight = weight
#         self.height = height

#     def __hash__(self):
#         return hash((self.weight, self.height))
    
# # taks 6

# class ShopItem:

#     def __init__(self, name:str, weight, price):
#         self.name = name
#         self.weight = weight
#         self.price = price

#     def __hash__(self):
#         return hash((self.name.lower(), self.weight, self.price))
    
#     def __eq__(self, other):
#         return hash(self) == hash(other)

# # lst_in = list(map(str.strip, sys.stdin.readlines()))
# lst_in = ['Системный блок: 1500 75890.56',
#           'Монитор Samsung: 2000 34000',
#           'Клавиатура: 200.44 545',
#           'Монитор Samsung: 2000 34000']


# shop_items = dict()

# for item in lst_in:
#     name, p_w = item.split(':')
#     price, weight = p_w.split()
#     print(name, price, weight, sep="|")
#     s_item = ShopItem(name, price, weight)
#     if s_item in shop_items:
#         shop_items[s_item][1] += 1
#     else:
#         shop_items[s_item] = [s_item, 1]

# print(shop_items)

# # task 7
# import sys
# class DataBase:

#     def __init__(self, path: str):
#         self.path = path
#         self.dict_db = {} 
    
#     def write(self, record):
#         if record in self.dict_db:
#             self.dict_db[record].append(record)
#         else:
#             self.dict_db[record] = [record,]

#     def read(self, pk):
#         for recs in self.dict_db.values():
#             for rec in recs:
#                 if rec.pk == pk:
#                     return rec
    
#         return None


# class Record:
#     Index = 0
#     def __init__(self, fio, descr, old):
#         self.fio = fio
#         self.descr = descr
#         self.old = old
#         self.pk = Record.Index
#         Record.Index += 1
#     def __hash__(self):
#         return hash((self.fio.lower(), self.old))

#     def __eq__(self, other):
#         return hash(self) == hash(other)


# #lst_in = list(map(str.strip, sys.stdin.readlines()))
# lst_in = ['Балакирев С.М.; программист; 33',
#         'Кузнецов Н.И.; разведчик-нелегал; 35',
#         'Суворов А.В.; полководец; 42',
#         'Иванов И.И.; фигурант всех подобных списков; 26',
#         'Балакирев С.М.; преподаватель; 33',
#         ]


# db = DataBase('/path')

# for item in lst_in:
#     fio, desc, old = item.split('; ')
#     db.write(Record(fio, desc, int(old)))



# db22345 = DataBase('123')
# r1 = Record('fio', 'descr', 10)
# r2 = Record('fio', 'descr', 10)
# assert r1.pk != r2.pk, "равные значения атрибута pk у разных объектов класса Record"

# db22345.write(r2)
# r22 = db22345.read(r2.pk)
# assert r22.pk == r2.pk and r22.fio == r2.fio and r22.descr == r2.descr and r22.old == r2.old, "при операциях write и read прочитанный объект имеет неверные значения атрибутов"

# assert len(db22345.dict_db) == 1, "неверное число объектов в словаре dict_db"

# fio = lst_in[0].split(';')[0].strip()
# v = list(db.dict_db.values())
# if fio == "Балакирев С.М.":
#     assert len(v[0]) == 2 and len(v[1]) == 1 and len(v[2]) == 1 and len(v[3]) == 1, "неверно сформирован словарь dict_db"
    
# if fio == "Гейтс Б.":
#     assert len(v[0]) == 2 and len(v[1]) == 2 and len(v[2]) == 1 and len(v[3]) == 1, "неверно сформирован словарь dict_db"

# #task 8

# class BookStudy:

#     def __init__(self, name, author, year):
#         self.name = name
#         self.author = author
#         self.year = year
    
#     def __hash__(self):
#         return hash((self.name.lower(), self.author.lower()))
    
# lst_in = list(map(str.strip, sys.stdin.readlines()))
# books = set()
# for b in lst_in:
#     name, author, year = b.split('; ')
#     bk =BookStudy(name, author, int(year))
#     books.add(bk)

# unique_books = len(books)

# # task 9

# class Dimensions:

#     @staticmethod
#     def check_value(value):
#         return (isinstance(value, (int, float)) and value > 0)

#     def __init__(self, a, b, c):
#         self.a = a
#         self.b = b
#         self.c = c

#     @property
#     def a(self):
#         return self.__a

#     @a.setter
#     def a(self, value):
#         if self.check_value(value):
#             self.__a = value
#         else:
#             raise ValueError("габаритные размеры должны быть положительными числами")

#     @property
#     def b(self):
#         return self.__b

#     @b.setter
#     def b(self, value):
#         if self.check_value(value):
#             self.__b = value
#         else:
#             raise ValueError("габаритные размеры должны быть положительными числами")

#     @property
#     def c(self):
#         return self.__c

#     @c.setter
#     def c(self, value):
#         if self.check_value(value):
#             self.__c = value
#         else:
#             raise ValueError("габаритные размеры должны быть положительными числами")

#     def __hash__(self):
#         return hash((self.a, self.b, self.c))
    
#     def __eq__(self, other):
#         return hash(self) == hash(other)
    
#     def __ge__(self, other):
#         return hash(self) >= hash(other)
    
#     def __lt__(self, other):
#         return hash(self) < hash(other)
    
#     def __str__(self):
#         return f'a={self.a}, b={self.b}, c={self.c}'
    
# s_inp = input()  # эту строку (переменную s_inp) в программе не менять

# num = [[float(x) for x in (nums.split())] for nums in s_inp.split(';')]

# lst_dims = [] 
# for coord in num:
#     try:
#         d = Dimensions(*coord)
#         lst_dims.append(d)
#     except ValueError:
#         pass
    
# lst_dims.sort()
