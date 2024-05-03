from memory_profiler import profile
import timeit
from dataclasses import dataclass
from statistics import mean, fmean


@dataclass(slots=True)
class A_fast:
    a: int
    b: int


@dataclass(frozen=True)
class A_slow:
    a: int
    b: int
    
@profile
def code_to_test_fast():
    res = [A_fast(i, i + 1) for i in range(10000)]
    # fast class, fast mean
    
    return res

@profile
def code_to_test_slow():
    res = [A_slow(i, i + 1) for i in range(10000)]
    
    return res


a = code_to_test_fast()

b = code_to_test_slow()

# elapsed_time = timeit.timeit(code_to_test_fast, number=2)
# elapsed_time1 = timeit.timeit(code_to_test_slow, number=2)


# print("Total execution time default dataclass:", elapsed_time, "seconds")
# print("Total execution time with slots, no frozen, fmean:", elapsed_time1, "seconds")

