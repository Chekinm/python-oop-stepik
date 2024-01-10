from random import randint


class Cell:

    def __init__(self, mine=False, number=0, is_open=False):
        self.is_mine = mine
        self.number = number
        self.is_open = is_open

    @property
    def is_mine(self):
        return self.__is_mine

    @is_mine.setter
    def is_mine(self, is_mine):
        if isinstance(is_mine, bool):
            self.__is_mine = is_mine
        else:
            raise ValueError("недопустимое значение атрибута")

    @property
    def number(self):
        return self.__number

    @number.setter
    def number(self, number):
        if isinstance(number, int) and number in range(9):
            self.__number = number
        else:
            raise ValueError("недопустимое значение атрибута")

    @property
    def is_open(self):
        return self.__is_open

    @is_open.setter
    def is_open(self, is_open):
        if isinstance(is_open, bool):
            self.__is_open = is_open
        else:
            raise ValueError("недопустимое значение атрибута")

    def __bool__(self):
        return not self.is_open

    def __str__(self):
        if not self.is_open:
            return '#'
        if self.is_mine:
            return '*'
        return f'{self.number}'


class GamePole:
    __pole = None

    def __new__(cls, *args, **kwargs):
        if cls.__pole is None:
            cls.__pole = super().__new__(cls)
        return cls.__pole

    def __init__(self, n, m, total_mines):
        self.rows = n
        self.columns = m
        self.total_mines = total_mines
        self.init_pole()

    @property
    def pole(self):
        return self.__pole_cells
    
    def _set_around(self, x, y):
        for _x in range(x - 1, x + 2, 1):
            for _y in range(y - 1, y + 2, 1):
                if 0 <= _x < self.rows and 0 <= _y < self.columns:
                    self.pole[_x][_y].number += 1
                    self.pole[_x][_y].is_open = True

    def init_pole(self):
        mines = self.total_mines
        self.__pole_cells = tuple(tuple(Cell() for _ in range(self.columns)) for _ in range(self.rows))
        while mines > 0:
            x = randint(0, self.rows - 1)
            y = randint(0, self.columns - 1)
            if not self.pole[x][y].is_mine:
                self.pole[x][y].is_mine = True
                self._set_around(x, y)
                mines -= 1

    def open_cell(self, x, y):
        try:
            self.pole[x][y].is_open = True
        except IndexError:
            raise IndexError('некорректные индексы i, j клетки игрового поля')

    def show_pole(self):
        for _ in range(self.rows):
            print(*self.pole[_])


pole = GamePole(10, 20, 10)  # создается поле размерами 10x20 с общим числом мин 10
pole.init_pole()
if pole.pole[0][1]:
    pole.open_cell(0, 1)
if pole.pole[3][5]:
    pole.open_cell(3, 5)

pole.show_pole()