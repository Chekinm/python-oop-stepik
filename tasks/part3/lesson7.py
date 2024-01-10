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

