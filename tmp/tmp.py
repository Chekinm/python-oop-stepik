import timeit
from functools import reduce

for_test3 = """a = range(100000)
b = sum([i * i for i in a])"""

for_test4 = """a = range(100000)
b = sum(map(lambda x: x*x, a))"""

for_test5 = """from functools import reduce
a = range(100000)
b = reduce(lambda sum, x: sum + x*x, a, 0)"""

print('Start')
el_time = timeit.timeit(for_test3, number=100)
el_time2 = timeit.timeit(for_test4, number=100)
el_time3 = timeit.timeit(for_test5, number=100)
print(f'{"List:":>5} {el_time}')
print(f'{"Map:":>5} {el_time2}')
print(f'{"reduce:":>5} {el_time3}')
