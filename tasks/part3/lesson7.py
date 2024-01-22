# task 4


# import sys

# class Player:

#     def __init__(self, name, old, score):
#         self.name = name
#         self.old = old
#         self.score = score
    
#     def __bool__(self):
#         return bool(self.score)

#     def __str__(self):
#         return f'{self.name=}, {self.score=}'


# # считывание списка из входного потока (эту строчку и список lst_in не менять)
# # lst_in = list(map(str.strip, sys.stdin.readlines()))
# lst_in = [
# "Балакирев; 34; 2048",
# "Mediel; 27; 0",
# "Влад; 18; 9012",
# "Nina P; 33; 0",
# ]

# players = []
# for line in lst_in:
#     name, old, score = line.split('; ')
#     players.append(Player(name, int(old), int(score)))

# players.filter(bool)

# print(*players)


# task 5

# import sys


# class MailItem:

#     def __init__(self, mail_from, title, content):
#         self.mail_from = mail_from
#         self.title = title
#         self.content = content
#         self.is_read = False

#     def set_read(self, fl_read):
#         self.is_read = fl_read

#     def __bool__(self):
#         return self.is_read


# class MailBox:

#     def __init__(self):
#         self.inbox_list = []

#     def receive(self):
#         lst_in = list(map(str.strip, sys.stdin.readlines()))
#         for line in lst_in:
#             self.inbox_list.append(MailItem(*line.split('; ')))


# mail = MailBox()

# mail.receive()
# mail.inbox_list[0].set_read(True)
# mail.inbox_list[-1].set_read(True)

# inbox_list_filtered = list(filter(bool, mail.inbox_list))

# # task 6

# class Line:

#     def __init__(self, x1, y1, x2, y2):
#         self.x1 = x1
#         self.y1 = y1
#         self.x2 = x2
#         self.y2 = y2
#         self.line_length = ((x2 - x1) ** 2 + (y2 - y1) ** 2) ** 0.5


#     def __len__(self):
#         return int(self.line_length)


# task 7


# class Ellipse :

#     def __init__(self, *args):
#         if args and len(args) == 4:
#             x1, x2, y1, y2 = args
#             self.x1 = x1
#             self.y1 = y1
#             self.x2 = x2
#             self.y2 = y2
#             self.is_described = True
#         else:
#             self.is_described = False
            
#     def __bool__(self):
#         return self.is_described

#     def __str__(self):
#         if self:
#             return "no coordinate"
#         else:
#             return f'{self.x1}, {self.y1}, {self.x2}, {self.y2}'
    
#     def get_coords(self):
#         try:
#             return (self.x1, self.x2, self.x2, self.y2)
#         except AttributeError:
#             raise AttributeError('нет координат для извлечения')
        

# lst_geom = [Ellipse(), Ellipse(1, 2, 3, 4), Ellipse(), Ellipse(10, 20, 30, 40)]

# for elip in lst_geom:
#     if elip:
#         elip.get_coords()


# task 9

class Vector:

    def __init__(self, *coords):
        self.coords = list(coords)
        self.dim = len(coords)
    
    def __add__(self, other):
        if self.dim == other.dim:
            return Vector(*tuple(map(lambda x, y: x + y, self.coords, other.coords)))
        else:
            raise ArithmeticError('размерности векторов не совпадают')

    def __sub__(self, other):
        if self.dim == other.dim:
            return Vector(*tuple(map(lambda x, y: x - y, self.coords, other.coords)))
        else:
            raise ArithmeticError('размерности векторов не совпадают')

    def __mul__(self, other):
        if self.dim == other.dim:
            return Vector(*tuple(map(lambda x, y: x * y, self.coords, other.coords)))
        else:
            raise ArithmeticError('размерности векторов не совпадают')

    def __iadd__(self, other):
        if isinstance(other, Vector):
            if self.dim == other.dim:
                for i in range(self.dim):
                    self.coords[i] += other.coords[i]
                return self
            else:
                raise ArithmeticError('размерности векторов не совпадают')
        for i in range(self.dim):
            self.coords[i] += other
        return self
    
    def __isub__(self, other):
        if isinstance(other, Vector):
            if self.dim == other.dim:
                for i in range(self.dim):
                    self.coords[i] -= other.coords[i] 
                return self
            else:
                raise ArithmeticError('размерности векторов не совпадают')
        for i in range(self.dim):
            self.coords[i] -= other
        return self
    
    def __imul__(self, other):
        if isinstance(other, Vector):
            if self.dim == other.dim:
                for i in range(self.dim):
                    self.coords[i] *= other.coords[i] 
                return self
            else:
                raise ArithmeticError('размерности векторов не совпадают')
        for i in range(self.dim):
            self.coords[i] *= other
        return self

    def __eq__(self, other):
        if self.dim != other.dim:
            return False
        for i in range(self.dim):
            if self.coords[i] != other.coords[i]:
                return False
        return True
            
            



a = Vector(1, 2, 3)
b = Vector(10, 20, 30)
c = a + b
c -= a

print(c == a)
