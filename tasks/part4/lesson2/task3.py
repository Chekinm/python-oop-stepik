class ListInteger(list):

    @staticmethod
    def _check_val(num):
        if not isinstance(num, int):
            raise TypeError('можно передавать только целочисленные значения')


    def __init__(self, iterable):
        for num in iterable:
            self._check_val(num)
        super().__init__(iterable)

    def append(self, num):
        self._check_val(num)
        super().append(num)

    def __setitem__(self, ind, num):
        self._check_val(num)
        super().__setitem__(ind, num)