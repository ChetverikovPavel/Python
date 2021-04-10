number = int(input('Введите число от нуля до 20: '))

if number == 1:
    print(number, 'процент')
elif number in range(2, 5):
    print(number, 'процента')
else:
    print(number, 'процентов')
