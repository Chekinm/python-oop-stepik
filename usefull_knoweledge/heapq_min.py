import heapq
from heapq import heapify, heappop, heappush
class SparseTable:

    def __init__(self):
        self.cols_list = [1]
        self.rows_list = [1]
        self.table = {}

    @property
    def rows(self):
        return 1 - self.rows_list[0]

    @property
    def cols(self):
        return 1 - self.cols_list[0]

    def _check_ind(self, *inds):
        for ind in inds:
            if not (isinstance(ind, int) and ind >= 0):
                raise IndexError('index must be non negative integer')

    def add_data(self, row, col, cell):
        self._check_ind(row, col)
        self.table[(row, col)] = cell
        heappush(self.cols_list, -1 * col)
        heappush(self.rows_list, -1 * row)

    def remove_data(self, row, col):
        self._check_ind(row, col)
        try:
            self.table.pop((row, col))
            self.cols_list.remove(-1 * col)

            self.rows_list.remove(-1 * row)

        except KeyError:
            raise IndexError('данные по указанным индексам отсутствуют')

    def get_data(self, row, col):
        self._check_ind(row, col)
        try:
            return self.table[(row, col)].value
        except KeyError:
            raise ValueError('данные по указанным индексам отсутствуют')

    def __getitem__(self, ind):
        row, col = ind
        return self.get_data(row, col)

    def __setitem__(self, ind, value):
        row, col = ind
        self.add_data(row, col, Cell(value))


class Cell:

    def __init__(self, value):
        self.value = value


st = SparseTable()
st.add_data(2, 5, Cell(25))
st.add_data(1, 1, Cell(11))
assert st.rows == 3 and st.cols == 6, "неверные значения атрибутов rows и cols"

try:
    v = st[3, 2]
except ValueError:
    assert True
else:
    assert False, "не сгенерировалось исключение ValueError"

st[3, 2] = 100
assert st[3, 2] == 100, "неверно отработал оператор присваивания нового значения в ячейку таблицы"
assert st.rows == 4 and st.cols == 6, "неверные значения атрибутов rows и cols"

st[4, 7] = 132
assert st.rows == 5 and st.cols == 8, "неверные значения атрибутов rows и cols"

st.remove_data(4, 7)
assert st.rows == 4 and st.cols == 6, "неверные значения атрибутов rows и cols, возможно, некорректно отработал метод remove_data"

st.remove_data(1, 1)
try:
    v = st[1, 1]
except ValueError:
    assert True
else:
    assert False, "не сгенерировалось исключение ValueError"
    
try:
    st.remove_data(1, 1)
except IndexError:
    assert True
else:
    assert False, "не сгенерировалось исключение IndexError"

d = Cell('5')
assert d.value == '5', "неверное значение атрибута value в объекте класса Cell, возможно, некорректно работает инициализатор класса"
st[11, 11] = 2
st[12, 12] = 3
st[100, 100] = 4
st[24, 24] = 5
st[110, 110] = 6
print(heappop(st.rows_list))
st.remove_data(12,12)

print(heappop(st.rows_list))
print(heappop(st.rows_list))
print(heappop(st.rows_list))