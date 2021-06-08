# Задание 4

def val_checker(verbosity=0):
    def get_num(func):
        def validator(*args):
            num = func(*args)
            if verbosity(*args):
                return num
            else:
                raise ValueError(f'ValueError: wrong val {args}')
            return num
        return validator
    return get_num


@val_checker(lambda x: x > 0)
def calc_cube(x):
    return x ** 3

a = calc_cube(10)
print(a)
print(calc_cube.__name__)