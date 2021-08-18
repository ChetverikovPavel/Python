n = 15
odd_num_gen = (num for num in range(1, n + 1) if num % 2)

# odd_num = 0  # Вариант вывода результата через next()
# while odd_num < n - 1:
#     odd_num = next(odd_num_gen)
#     print(odd_num)

for odd_num in odd_num_gen:
    print(odd_num)