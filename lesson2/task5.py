my_num_list = [57.8, 46.51, 97, 25, 39.7, 92.15, 57.13, 19.08, 46, 11.02, 75]

# Задание A
i = 0
while True:
    if i + 1 == len(my_num_list):
        print(f"{int(my_num_list[i])} руб {int((my_num_list[i] * 100 % 100)):02d} коп", end='\n\n')
        break
    else:
        print(f"{int(my_num_list[i])} руб {int((my_num_list[i] * 100 % 100)):02d} коп", end=", ")
    i += 1

# Задание B
print('Проверка того, что объект списка после сортировки остался тот же')
print(my_num_list)
print(id(my_num_list))
my_num_list.sort()
print(my_num_list)
print(id(my_num_list), end='\n\n')

i = 0
print('Список по возрастанию')
while True:
    if i + 1 == len(my_num_list):
        print(f"{int(my_num_list[i])} руб {int((my_num_list[i] * 100 % 100)):02d} коп", end='\n\n')
        break
    else:
        print(f"{int(my_num_list[i])} руб {int((my_num_list[i] * 100 % 100)):02d} коп", end=", ")
    i += 1

# Задание C
my_revers_list = sorted(my_num_list, reverse=True)
i = 0
print('Список по убыванию')
while True:
    if i + 1 == len(my_revers_list):
        print(f"{int(my_revers_list[i])} руб {int((my_revers_list[i] * 100 % 100)):02d} коп", end='\n\n')
        break
    else:
        print(f"{int(my_revers_list[i])} руб {int((my_revers_list[i] * 100 % 100)):02d} коп", end=", ")
    i += 1

# Задание D
max_price_list = sorted(my_revers_list[0:4])
i = 0
print('Пять самых дорогих товаров по возрастанию')
while True:
    if i + 1 == len(max_price_list):
        print(f"{int(max_price_list[i])} руб {int((max_price_list[i] * 100 % 100)):02d} коп")
        break
    else:
        print(f"{int(max_price_list[i])} руб {int((max_price_list[i] * 100 % 100)):02d} коп", end=", ")
    i += 1
