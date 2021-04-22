from time import perf_counter
from sys import getsizeof

# Реализация через генератор
start = perf_counter()
src = [300, 2, 12, 44, 1, 1, 4, 10, 7, 1, 78, 123, 55]
src_gen = (num for num in src)
temp_num = 0
result = []
print('Генератор:', getsizeof(src_gen))
for el in src_gen:
    if not temp_num:
        temp_num = el
        continue
    if temp_num < el:
        result.append(el)
    temp_num = el
print(perf_counter() - start)
print(result)

# Реализация через список
start = perf_counter()
src = [300, 2, 12, 44, 1, 1, 4, 10, 7, 1, 78, 123, 55]
result2 = []
temp_num = 0
print('Список:', getsizeof(src))
for el in src:
    if not temp_num:
        temp_num = el
        continue
    if temp_num < el:
        result2.append(el)
    temp_num = el
print(perf_counter() - start)
print(result2)
# Реализация через генератор работает медленнее (в данном случае)
# Реализация через генератор использует меньше памяти