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
