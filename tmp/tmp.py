from collections import Counter

a = ['1', 1, True]
b = Counter((i, type(i)) for i in a)
print(b)