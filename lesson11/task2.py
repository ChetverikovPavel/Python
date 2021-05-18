class ZeroError(Exception):
    def __init__(self, txt):
        self.txt = txt


try:
    input_num_1 = int(input('Введите делимое: '))
    input_num_2 = int(input('Введите делитель: '))
    if input_num_2 == 0:
        raise ZeroError('На ноль делить нельзя')
except ZeroError as err:
    print(err)
    input_num_2 = int(input('Введите другой делитель: '))
finally:
    print(f'Результат деления: {input_num_1 / input_num_2}')