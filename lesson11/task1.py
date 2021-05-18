import time


class MyException(Exception):
    def __init__(self, txt):
        self.txt = txt


class Date:

    def __init__(self, date_str):
        try:
            if (type(date_str) is str) and (date_str.count('-') == 2):
                self.date_str = date_str
            else:
                raise MyException('Необходимо ввести строку в формате: «день-месяц-год»')
        except MyException as err:
            print(err)

    @classmethod
    def date_to_number(cls, param):
        f_result = list(map(int, param.split('-')))
        return f_result

    @staticmethod
    def date_check(date):
        print(f'\n{date}')
        try:
            time.strptime(date, '%d-%m-%Y')
            return 'Дата верна'
        except ValueError:
            return 'Неверная дата'


date_2 = Date('15152020')
date_1 = Date('13-05-2015')

print(date_1.date_to_number(date_1.date_str))
print(date_1.date_check(date_1.date_str))

print(Date.date_to_number('28-02-2021'))
print(Date.date_check('28-02-2021'))
print(Date.date_check('31-02-2021'))
print(Date.date_check('11-13-2021'))

