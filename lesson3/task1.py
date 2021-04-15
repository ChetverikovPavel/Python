def num_translate_adv(number):
    flag = 0
    numbers = {'zero': 'ноль', 'one': 'один', 'two': 'два', 'three': 'три', 'four': 'четыре',
               'five': 'пять', 'six': 'шесть', 'seven': 'семь', 'eight': 'восемь',
               'nine': 'девять', 'ten': 'десять'}
    if number.istitle():
        number = number.lower()
        flag = 1
    if number in numbers:
        if flag:
            return numbers[number].title()
        else:
            return numbers[number]
    else:
        return


#  Проверка работы функции
print(num_translate_adv('zero'))
print(num_translate_adv('one'))
print(num_translate_adv('two'))
print(num_translate_adv('three'))
print(num_translate_adv('four'))
print(num_translate_adv('five'))
print(num_translate_adv('six'))
print(num_translate_adv('seven'))
print(num_translate_adv('eight'))
print(num_translate_adv('nine'))
print(num_translate_adv('ten'))
print(num_translate_adv('Eight'))
print(num_translate_adv('Ten'))
print(num_translate_adv('8'))
print(num_translate_adv('abcd'))
