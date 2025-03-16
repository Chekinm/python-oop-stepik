
from datetime import datetime


class DateString:
    def __init__(self, date_string):
        try:
            self.date_string = datetime.strptime(date_string, "%d.%m.%Y")
        except ValueError:
            raise DateError

    def __str__(self):
        return self.date_string.strftime("%d.%m.%Y")


class DateError(Exception):
    def __str__(self):
        return "Неверный формат даты"


d = "1.2.1812"
nd = DateString(d)
print(nd)
