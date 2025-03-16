class ValidatorString:      

    def __init__(self, min_length, max_length, chars):
        self.min_length = min_length
        self.max_length = max_length
        self.chars = chars

    def is_valid(self, string):
        if (len(self.chars) and
            (len(set(self.chars).intersection(set(string))) == 0 or
             not self.min_length <= len(string) <= self.max_length)):
            raise ValueError('недопустимая строка')


class LoginForm:

    def __init__(self, login_validator: ValidatorString, password_validator: ValidatorString):
        self.login_validator = login_validator
        self.password_validator = password_validator
    
    def form(self, request):
        try:
            self.login_validator.is_valid(request['login'])
            self.password_validator.is_valid(request['password'])
        except KeyError:
            raise TypeError('в запросе отсутствует логин или пароль')
        except ValueError:
            raise ValueError('недопустимая строка')
        else:
            self._login = request['login']
            self._password = request['password']
    
login_v = ValidatorString(4, 50, "")
password_v = ValidatorString(10, 50, "!$#@%&?")
lg = LoginForm(login_v, password_v)
login, password = input().split()
try:
    lg.form({'login': login, 'password': password})
except (TypeError, ValueError) as e:
    print(e)
else:
    print(lg._login)