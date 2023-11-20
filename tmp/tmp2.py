from math import sqrt



def erast():
    ans = [True] * 10001
    for i in range(2, 101):
        if ans[i]:
            k = 2
            while i * k < 10001:
                ans[i * k] = False
                k += 1

    return list(filter(lambda x: ans[x], range(2, 10001)))


def find_e(p, query):
    if not query(p, 1):
        return 0
    e_min = 0
    e_max = 10 ** 9
    e_mid_prev = 0
    while e_max - e_min > 0:
        e_mid = (e_max + e_min) // 2
        if query(p, e_mid):
            e_min = e_mid
        else:
            e_max = e_mid

        if e_mid == e_mid_prev:
            break
        else:
            e_mid_prev = e_mid
    return e_mid


def play(query):

    prime = erast()
    number = []
    for p in prime:
        e = find_e(p, query)
        if e:
            number.append((p, e))
#     for p, e in number:
#         if e > 1:
#             return 2
   
    return number