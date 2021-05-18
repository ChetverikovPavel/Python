class NotNumError(Exception):
    def __init__(self, txt):
        self.txt = txt


num_list = []
while True:
    try:
        input_num = input('Введите число: ')
        if input_num == 'stop':
            print(num_list)
            break
        if not input_num.isdigit():
            raise NotNumError('Вы ввели не число')
        else:
            num_list.append(input_num)
    except NotNumError as err:
        print(err)

