
def hyper_outer(attr):
    c = 23
    def outer_function():
        x = 10

        def inner_function():
            y = 20
            print("Область видимости внутренней функции:", attr, vars())

        print("Область видимости внешней функции:", vars())
        return inner_function
    return outer_function



a = hyper_outer('sadfsdf')
b = a()
b()