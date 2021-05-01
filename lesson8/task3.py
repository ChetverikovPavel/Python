from functools import wraps


def type_logger(callback):
    @wraps(callback)
    def wrapper(*args):
        for el in args:
            print(f"{calc_cube.__name__}({el}: {type(el)})", end=', ')

    return wrapper


@type_logger
def calc_cube(*x):
    cube_list = []
    for el in x:
        cube_list.append(el ** 3)

    return tuple(cube_list)


numbers = (5, 6, 4)
calc_cube(*numbers)
