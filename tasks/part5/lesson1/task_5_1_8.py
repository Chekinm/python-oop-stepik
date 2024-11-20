lst_in = "1 -5.6 True abc 0 23.56 hello".split()


def convert_type(value):
    converted_value = None
    try:
        converted_value = float(value)
        converted_value = int(value)
    except ValueError:
        converted_value = converted_value if converted_value else value
    finally:
        return converted_value 


lst_out = list(map(convert_type, lst_in))
print(lst_out)
