duration = int(input('Введите число секунд: '))
s = duration % 60
m = duration // 60 % 60
h = duration // 3600 % 24
d = duration // (3600 * 24)

print('duration =', duration)
if duration < 60:  # Меньше минуты. Выводится количество секунд.
    print(s, 'сек')
elif duration < 60 * 60:  # Меньше часа. Выводится количество минут и секунд.
    print(m, 'мин', s, 'сек')
elif duration < 60 * 60 * 24:  # Меньше суток. Выводится количество часов, минут и секунд.
    print(h, 'час', m, 'мин', s, 'сек')
else:  # Больше сутов. Выводится количество дней, часов, минут и секунд.
    print(d, 'дн', h, 'час', m, 'мин', s, 'сек')
