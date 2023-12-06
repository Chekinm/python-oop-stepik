# # task 3
# from math import sqrt

# class TrackLine:

#     def __init__(self, to_x, to_y, max_speed):
#         self.to_x = to_x
#         self.to_y = to_y
#         self.max_speed = max_speed


# class Track:

#     def __init__(self, start_x, start_y):

#         self.start_x = start_x
#         self.start_y = start_y
#         self.lines = []
#         self.curr_x = start_x
#         self.curr_y = start_y
#         self.lenght = 0

#     def add_track(self, tr):

#         if isinstance(tr, TrackLine):
#             self.lines.append(tr)
#             x, y, speed = tr.to_x, tr.to_y, tr.max_speed
#             self.lenght += sqrt((x- self.curr_x) ** 2 + (y - self.curr_y) ** 2)
#             self.curr_x, self.curr_y = x, y
#         else:
#             raise TypeError('track supposed to be an instance of TrackLine class')

#     def get_tracks(self):
#         return tuple(self.lines)

#     def __len__(self):
#         return int(self.lenght)

#     def __eq__(self, other):
#         if isinstance(other, Track):
#             return self.lenght == other.lenght
        
#     def __gt__(self, other):
#         if isinstance(other, Track):
#             return self.lenght > other.lenght

# track1 = Track(0, 0)
# track2 = Track(0, 1)

# track1.add_track(TrackLine(2, 4, 100))
# track1.add_track(TrackLine(5, -4, 100))

# track2.add_track(TrackLine(3, 2, 90))
# track2.add_track(TrackLine(10, 8, 90))

# res_eq = track1 == track2


# # task 4
# from dataclasses import dataclass


# class Dimensions:

#     MIN_DIMENSION = 10
#     MAX_DIMENSION = 10000

#     @classmethod
#     def _check_dimension(cls, size):
#         return cls.MIN_DIMENSION <= size <= cls.MAX_DIMENSION

#     def __init__(self, a, b, c):
#         self.a = a
#         self.b = b
#         self.c = c

#     @property
#     def a(self):
#         return self.__a

#     @a.setter
#     def a(self, a):
#         if self._check_dimension(a):
#             self.__a = a

#     @property
#     def b(self):
#         return self.__b

#     @b.setter
#     def b(self, b):
#         if self._check_dimension(b):
#             self.__b = b

#     @property
#     def c(self):
#         return self.__c

#     @c.setter
#     def c(self, c):
#         if self._check_dimension(c):
#             self.__c = c

#     @property
#     def volume(self):
#         return self.a * self.b * self.c


#     def __gt__(self, other):
#         if isinstance(other, Dimensions):
#             return self.volume > other.volume
#         else:
#             raise NotImplementedError(f'cannot compare {type(self)} with {type(other)}')

#     def __ge__(self, other):
#         if isinstance(other, Dimensions):
#             return self.volume >= other.volume
#         else:
#             raise NotImplementedError(f'cannot compare {type(self)} with {type(other)}')

#     def __str__(self):
#         return f'Dimensions: a={self.a}, b={self.b}, c={self.c}'
    
#     def __repr__(self):
#         return f'Dimensions: a={self.a}, b={self.b}, c={self.c}'

# @dataclass
# class ShopItem:
#     name: str
#     price: str | float 
#     dim: Dimensions

#     def __init__(self, name: str, price: int | float, dim: Dimensions) -> None:

#         self.name = name
#         self.price = price
#         self.dim = dim

#     def volume(self):
#         return self.dim.volume


# lst_shop = [ShopItem('кеды',1024, Dimensions(40, 30, 120)),
#             ShopItem('зонт',500.24, Dimensions(10, 20, 50)),
#             ShopItem('холодильник',40000, Dimensions(2000, 600, 500)),
#             ShopItem('табуретка',2000.99, Dimensions(500, 200, 200)),
#             ]

# lst_shop_sorted = sorted(lst_shop, key=ShopItem.volume)
# print(lst_shop_sorted)

# # task 5

# class StringText:

#     def __init__(self, lst_words):
#         self.lst_words = lst_words
#         self.lenght = len(self.lst_words)
    
#     def __repr__(self):
#         return ' '.join(self.lst_words)
    
#     def __len__(self):
#         return len(self.lst_words)
    
#     def __gt__(self, other):
#         if isinstance(other, StringText):
            
#             return len(self) > len(other)

#     def __ge__(self, other):
#         if isinstance(other, StringText):
#             return len(self) >= len(other)

# simbols = "–?!,.;"

# stich = ["Я к вам пишу – чего же боле?",
#          "Что я могу еще сказать?",
#          "Теперь, я знаю, в вашей воле",
#          "Меня презреньем наказать.",
#          "Но вы, к моей несчастной доле",
#          "Хоть каплю жалости храня,",
#          "Вы не оставите меня.",
#          ]

# lst_text = []
# for string in stich:
#     string = string.replace('–','')
#     string_lst = string.split()
#     for i in range(len(string_lst)):
#         string_lst[i] = string_lst[i].strip(simbols)
        
#     lst_text.append(StringText(string_lst))

# lst_text_sorted = sorted(lst_text, reverse=True)

# lst_text_sorted = [' '.join(string.lst_words) for string in lst_text_sorted]

# print(lst_text_sorted)


# # task 6

# class Morph:

#     def __init__(self, *words):
#         self.words = []
#         for word in words:
#             self.words.append(word.lower())
        
        
#     def add_word(self, word):
#         if word.lower() not in self.words:
#             self.words.append(word.lower())

#     def get_words(self):
#         return tuple(self.words)

#     def __eq__(self, other):
#         if isinstance(other, str):
#             return other.lower() in self.words
        
    


# dict_words = [Morph('связь', 'связи', 'связью', 'связи', 'связей', 'связям', 'связями', 'связях'),
#               Morph('формула', 'формулы', 'формуле', 'формулу', 'формулой', 'формул', 'формулам', 'формулами',
#                     'формулах',
#                     ),
#               Morph('вектор', 'вектора', 'вектору', 'вектором', 'векторе', 'векторы', 'векторов', 'векторам',
#                     'векторами', 'векторах',
#                     ),
#               Morph('эффект', 'эффекта', 'эффекту', 'эффектом', 'эффекте', 'эффекты', 'эффектов', 'эффектам',
#                     'эффектами', 'эффектах'
#                     ), 
#               Morph('день', 'дня', 'дню', 'днем', 'дне', 'дни', 'дням', 'днями', 'днях',
#                     )]

# # text = input()
# text = "Мы будем устанавливать связь завтра днем."
# t = text.strip(' .,!?').split()
# print(t)
# count = 0
# for word in t:
#     for mf in dict_words:
#         if word == mf:
#             count += 1

# print(count)

# for mf in dict_words:
#     print(mf.get_words())

# # task 7 

# class FileAcceptor:

#     def __init__(self, *exts):
#         self.exts = list(exts)

#     def __call__(self, filename):
#         ext = filename.split('.')[-1]
#         return ext in self.exts
    

#     def __add__(self, other):
#         res = FileAcceptor(*self.exts)
#         for ext in other.exts:
#             if ext not in res.exts:
#                 res.exts.append(ext)
#         return res
                
    
# # task 8

# class Currency:
#     RUB = 'rub'
#     DOLLAR = 'dollar'
#     EURO = 'euro'


# class CentralBank:

#     banks = []
#     def __new__(cls):
#         return None

#     rates = {'rub': 72.5, 'dollar': 1.0, 'euro': 1.15}

#     @classmethod
#     def register(cls, money):
#         money.cb = cls


# class Money:

#     def __init__(self, volume=0, currency=None):
#         self.volume = volume
#         self.cb = None
#         self.currency = currency

#     @property
#     def cb(self):
#         return self.__cb

#     @cb.setter
#     def cb(self, cb):
#         if hasattr(cb, 'rates'):
#             self.__cb = cb
#         else:
#             self.__cb = None

#     @property
#     def volume(self):
#         return self.__volume 

#     @volume.setter
#     def volume(self, volume):
#         if isinstance(volume, (int, float)):
#             self.__volume = volume

#     @property
#     def _is_rigestred(self):
#         if self.currency is None or self.cb is None:
#             return False
#         return True

#     def __eq__(self, other):
#         if not self._is_rigestred:
#             raise ValueError("Неизвестен курс валют.")

#         return abs(self.volume / self.cb.rates[self.currency] -
#                    other.volume / other.cb.rates[other.currency]) < 0.1

#     def __gt__(self, other):
#         if not self._is_rigestred:
#             raise ValueError("Неизвестен курс валют.")

#         print(f'self - {self.currency} in usd, {self.volume / self.cb.rates[self.currency]}')
#         print(f'other -{other.currency} in usd, {other.volume / other.cb.rates[self.currency]}')


#         return (self.volume / self.cb.rates[self.currency] > 
#                 other.volume / other.cb.rates[other.currency]) 

#     def __ge__(self, other):
#         if not self._is_rigestred:
#             raise ValueError("Неизвестен курс валют.")

#         return (self.volume / self.cb.rates[self.currency] >=
#                 other.volume / other.cb.rates[other.currency]) 
    

# class MoneyR(Money):

#     def __init__(self, volume):
#         super().__init__(volume, currency=Currency.RUB)
#         self.cb = None


# class MoneyD(Money):

#     def __init__(self, volume):
#         super().__init__(volume, Currency.DOLLAR)


# class MoneyE(Money):

#     def __init__(self, volume):
#         super().__init__(volume, Currency.EURO)


# CentralBank.rates = {'rub': 10, 'dollar': 1.0, 'euro': 2}
# print(CentralBank.rates)

# r = MoneyR(45000)
# d = MoneyD(500)

# CentralBank.register(r)
# CentralBank.register(d)
# print(r.cb.rates)


# r = MoneyR(45000)
# d = MoneyD(500)

# CentralBank.register(r)
# CentralBank.register(d)

# print(r.currency)
# print(d.currency)

# if r > d:
#     print("неплохо")
# else:
#     print("нужно поднажать")

# # task 9

# class Body:

#     def __init__(self, name, ro, volume):
#         self.name = name
#         self.ro = ro
#         self. volume = volume
#         self.mass = ro * volume

#     def __eq__(self, other):
#         other = other.mass if isinstance(other, Body) else other
#         return self.mass == other

#     def __lt__(self, other):
#         other = other.mass if isinstance(other, Body) else other
#         return self.mass < other


# body1 = Body('s',1,1000)
# body2 = Body('d',2,300)

# print(body1.mass)
# print(body2.mass)
# print(body1<body2)

# print(body1>body2)
