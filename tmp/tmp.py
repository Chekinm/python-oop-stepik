from datetime import datetime
def cashed(func):
    memo_dict = {}

    def wrapper(*args, **kwargs):
        arg_key = (*args, tuple(kwargs.items()))
        if arg_key not in memo_dict:
            memo_dict[arg_key] = func(*args, **kwargs)
        print(memo_dict)
        return memo_dict[arg_key]

    return wrapper

def repeater(n=2):
    def rep_wraper(func):

        def wraper(*args, **kwargs):
            for _ in range(n):
                res = func(*args, **kwargs)
            return res
        
        return wraper
        
    return rep_wraper



@cashed
def f(a, b, c=200):
    res = a * b * c
    print(f'Function called {res=}')
    return res



count = 0

@repeater(3)
def f1(a, b=2):
    
    global count
    count += 1
    print(count)
    return a * b * count

print(f1(3, b=2))