class StringDigit(str):
    def __new__(cls, string):
        try:
            int(string)
            instance = super().__new__(cls, string)
            return instance
        except ValueError:
            raise ValueError("в строке должны быть только цифры")

    def __init__(self, string):
        self.value = string

    def __add__(self, other):
        digit_other = StringDigit(other)
        return StringDigit(super().__add__(digit_other))

    def __radd__(self, other):
        digit_other = StringDigit(other)
        return StringDigit(digit_other + self.value)

sd = StringDigit("123")
print(sd)       # 123
sd = sd + "456" # StringDigit: 123456
print(sd)
sd = "789" + sd # StringDigit: 789123456
print(sd)
sd = sd + "12f" # ValueError
print(sd)