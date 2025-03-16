class PrimaryKeyError(Exception):
    def __init__(self, id=None, pk=None):
        if not (id or pk):
            self.message = "Первичный ключ должен быть целым неотрицательным числом"
        elif id is not None:
            self.message = f"Значение первичного ключа id = {id} недопустимо"
        elif pk is not None:
            self.message = f"Значение первичного ключа pk = {pk} недопустимо"
        else:
            self.message = "Другая ошибка"
          
try:
    raise PrimaryKeyError(id=-10.5)
except PrimaryKeyError as error:
    print(error)