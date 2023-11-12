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
