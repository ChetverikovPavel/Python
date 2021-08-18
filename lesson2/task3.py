my_list = ['в', '5', 'часов', '17', 'минут', 'температура', 'воздуха', 'была', '+5', 'градусов']

i = 0
while i < len(my_list):
    if my_list[i].isdigit() or '+' in my_list[i]:
        if my_list[i].isdigit():
            my_list[i] = f'{int(my_list[i]):02d}'
        else:
            my_list[i] = f'+{int(my_list[i]):02d}'
        my_list.insert(i, '"')
        my_list.insert(i + 2, '"')
        i += 3
    else:
        i += 1
print(my_list)

i = 0
while i < len(my_list):
    if my_list[i].isdigit() or '+' in my_list[i]:
        my_list[i - 1] = ''.join(my_list[i - 1:i + 2])
        del my_list[i:i + 2]
    i += 1
print(my_list)

result_str = ' '.join(my_list[:])
print(result_str)
