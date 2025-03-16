def get_div(x, y):
    try:
        res = x / y
        res = list((res,))
        print(res)
        return res
    except ZeroDivisionError:
        res = 100
        return res
    finally:
        res[0] = -1
        print(f"finally: {res[0]}")
        

a = get_div(1, 2)
print(a)