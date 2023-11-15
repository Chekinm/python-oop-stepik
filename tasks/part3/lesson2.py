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