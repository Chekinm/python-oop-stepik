# 

# # task 7

# from string import ascii_lowercase, digits


# class TextInput:
#     CHARS = "абвгдеёжзийклмнопрстуфхцчшщьыъэюя " + ascii_lowercase
#     CHARS_CORRECT = CHARS + CHARS.upper() + digits

#     @classmethod
#     def check_name(cls, name):
#         return (3 <= len(name) <= 50 and
#                 set(name).issubset(set(cls.CHARS_CORRECT)))

#     def __init__(self, name, size=10):
#         if self.check_name(name):
#             self.name = name
#             self.size = size
#         else:
#             raise ValueError("некорректное поле name")

#     def get_html(self):
#         return f"<p class='login'>{self.name}: <input type='text' size={self.size} />"


# class PasswordInput:
#     CHARS = "абвгдеёжзийклмнопрстуфхцчшщьыъэюя " + ascii_lowercase
#     CHARS_CORRECT = CHARS + CHARS.upper() + digits

#     @classmethod
#     def check_name(cls, name):
#         return (3 <= len(name) <= 50 and
#                 set(name).issubset(set(cls.CHARS_CORRECT)))
    
#     def __init__(self, name, size=10):
#         if self.check_name(name):
#             self.name = name
#             self.size = size
#         else: 
#             raise ValueError("некорректное поле name")

#     def get_html(self):
#         return f"<p class='password'>{self.name}: <input type='text' size={self.size} />"


# class FormLogin:
#     def __init__(self, lgn, psw):
#         self.login = lgn
#         self.password = psw

#     def render_template(self):
#         return "\n".join(['<form action="#">', self.login.get_html(), self.password.get_html(), '</form>'])


# # эти строчки не менять
# login = FormLogin(TextInput("Логин"), PasswordInput("Пароль"))
# html = login.render_template()

# # task 8

# from string import ascii_lowercase, digits
# import re


# class CardCheck:

#     @staticmethod
#     def check_card_number(number):
#         pattern = r'\d{4}-\d{4}-\d{4}-\d{4}'
#         return bool(re.fullmatch(pattern, number, flags=0))
    
#     @staticmethod
#     def check_name(name):
#         CHARS_FOR_NAME = ascii_lowercase.upper() + digits 
#         name_splitted = name.split()
#         return (len(name_splitted) == 2 and
#                 set(name_splitted[0]).issubset(set(CHARS_FOR_NAME)) and
#                 set(name_splitted[1]).issubset(set(CHARS_FOR_NAME)))

# a = "1234-2342-344-3545"
# print(CardCheck.check_card_number(a))

# # task 9

# class Video:

#     def create(self, name):
#         self.name = name

#     def play(self):
#         print(f'воспроизведение видео {self.name}')


# class YouTube:
#     _videos = []

#     @classmethod
#     def add_video(cls, video):
#         cls._videos.append(video)

#     @classmethod
#     def play(cls, video_indx):
#         try:
#             cls._videos[video_indx].play()
#         except IndexError:
#             print('wrong index')


# v1 = Video()
# v2 = Video()
# v1.create('Python')
# v2.create('Python ООП')

# YouTube.add_video(v1)
# YouTube.add_video(v2)

# YouTube.play(0)
# YouTube.play(1)

# # task 10

# class Applilcation:
#     def __init__(self, name, blocked=False):
#           self.name = name
#           self.blocked = blocked
    
#     @property 
#     def set_blocked(self):
#          self.blocked =True

#     @property
#     def set_unblocked(self):
#         self.blocked =False
    
# class AppStore:
    
#     def __init__(self):
#          self.apps_dict = {}
         
#     def add_application(self, app):
#         if app.name not in self.apps_dict:
#             self.apps_dict[app.name] = app

#     def remove_application(self, app):
#         if app.name in self.apps_dict:
#             self.apps_dict.pop(app.name)
#         else:
#             raise ValueError
         
#     def block_application(self, app):
#         if app.name in self.apps_dict:
#             self.apps_dict[app.name].set_blocked
#         else:
#             raise ValueError
    
#     def total_apps(self):
#         return len(self.apps_dict)
        
# task 11
