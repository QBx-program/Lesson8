#Задание 3

def type_log(func):
    def type_a(*args, **kwargs):
        if args:
            for num in args:
                print(f'{func(num)}: {type(func(num))}')
        if kwargs:
            for k, v in kwargs.items():
                print(f'key = {k}, value = {v}, {func(v)}: {type(func(v))}')
    return type_a

@type_log
def calc_cube(x=1):
    return x**3

calc_cube(2, 5, 8.9, 9.3, a=3, b=7.5)