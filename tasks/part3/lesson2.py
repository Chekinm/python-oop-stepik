# # task 2
# from random import randint, sample, choices

# a = 100

# class RandomPassword:

#     def __init__(self, psw_chars, min_length, max_length):

#         self.psw_chars = psw_chars
#         self.min_length = min_length
#         self.max_length = max_length

#     def __call__(self):
#         length = randint(self.min_length, self.max_length)
#         psw = ''.join(choices(psw_chars, k=length))
#         for i in psw:
#             if i not in psw_chars:
#                 print('wrong_char', i)
#         return psw


# def random_password_factory(psw_chars, min_length, max_length):

#     def rnd_pswd():
#         length = randint(min_length, max_length)
#         psw = ''.join(choices(psw_chars, k=length))
#         print('inside', globals())
#         return psw

#     return rnd_pswd




# min_length = 5
# max_length = 20
# psw_chars = "qwertyuiopasdfghjklzxcvbnm0123456789!@#$%&*"

# rnd1 = RandomPassword(psw_chars, min_length, max_length)
# rnd2 = random_password_factory(psw_chars, min_length, max_length)


# lst_pass1 = [rnd1() for _ in range(3)]
# lst_pass2 = [rnd2() for _ in range(3)]


# print(lst_pass1)
# print(lst_pass2)

# print(rnd1.__dict__)
# print(rnd2.__dict__)

# # task 3


# class ImageFileAcceptor:

#     def __init__(self, extensions: tuple[str]) -> None:
#         self.extensions = extensions

#     def __call__(self, file_name):
#         file_ext = file_name.split('.')[-1]
#         for ext in self.extensions:
#             if ext == file_ext:
#                 return True
#         return False


# filenames = ["", "web.png", "text.txt", "python.doc", "ava.jpg", "forest.jpeg", "eq_1.png", "eq_2.png"]
# acceptor = ImageFileAcceptor(('jpg', 'bmp', 'jpeg'))
# image_filenames = filter(acceptor, filenames)
# print(list(image_filenames))  # ["boat.jpg", "ava.jpg", "forest.jpeg"]

# task 4


class LengthValidator:
    def __init__(self, min_length, max_length):
        self.min_length = min_length
        self.max_length = max_length

    def __call__(self, string):
        if self.min_length <= len(string) <= self.max_length:
            return True
        return False


class CharsValidator:
    def __init__(self, chars):
        self.set_chars = set(chars)

    def __call__(self, string):
        if set(string).issubset(self.set_chars):
            return True
        return False


class LoginForm:
    def __init__(self, name, validators=None):
        self.name = name
        self.validators = validators
        self.login = ""
        self.password = ""
        
    def post(self, request):
        self.login = request.get('login', "")
        self.password = request.get('password', "")
        
    def is_validate(self):
        if not self.validators:
            return True
        
        for v in self.validators:
            if not v(self.login) or not v(self.password):
                return False
            
        return True