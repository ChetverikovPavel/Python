num_list = list(range(1, 1000, 2))
result_a = 0
result_b = 0
flag = 1

print(num_list)  # Вывод списка нечетных чисел

for number in num_list[:]:  # Возведение элементов списка в куб
    if flag:
        num_list.clear()
        flag = 0
    num_list.append(number ** 3)
print(num_list)  # Вывод списка с возведением элементов в куб

for number in num_list:  # Выполнение задания "a"
    sum_for_check = 0  # "Сумма для проверки". Сумма цифр числа для проверки условия
    temp_var = number  # Временная переменная для хранения промежуточных значений number
    while True:
        if temp_var == 0:
            break
        sum_for_check += temp_var % 10
        temp_var = temp_var // 10
    if sum_for_check % 7 == 0:
        result_a += number
print(result_a)  # Вывод результата задания "a"

for number in num_list:  # Выполнения задания "b"
    sum_for_check = 0
    temp_var = number + 17
    while True:
        if temp_var == 0:
            break
        sum_for_check += temp_var % 10
        temp_var = temp_var // 10
    if sum_for_check % 7 == 0:
        result_b += number + 17
print(result_b)  # Вывод результата задания "b"
