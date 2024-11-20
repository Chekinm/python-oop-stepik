def check_int(value):
    try:
        int(value)
        return True
    except ValueError:
        return False

l = "1 -5.6 2 abc 0 False 22.5 hello world"

lst_in = l.split()

print(sum(map(int, filter(check_int, lst_in))))

