from math import sqrt



def query(p, e):

    for i in range(2, int(sqrt(p))):
        if p % i == 0:
            return False

    k = p ** e
    return 34 % k == 0

def erast():
    ans = [True] * 10 ** 5
    for i in range(2, 100):
        if ans[i]:
            k = 2
            while i * k < 10001:
                ans[i * k] = False
                k += 1

    return list(filter(lambda x: ans[x], range(2, 10000)))


def find_e(p, query):
    e_min = 0
    e_max = 100
    e_mid = e_max
    e_mid_prev = 0
    while e_mid != e_mid_prev:
        e_mid = (e_max + e_min) // 2
        if query(p, e_mid):
            e_min = e_mid
        else:
            e_max = e_mid
            
        e_mid_prev = e_mid

    return e_mid

print(find_e(7, query))



# def play(query):

#     prime = erast()
#     number = []
#     for p in prime:
#         e = find_e(p, query)
#         if e:
#             number.append((p, e))

#     return number
