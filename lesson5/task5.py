from time import perf_counter

# Реализация без использования множеств для сравнения скорости
src = [2, 2, 2, 7, 23, 1, 44, 44, 3, 2, 10, 7, 4, 11]
start = perf_counter()
result = []
for el in src:
    if src.count(el) == 1:
        result.append(el)
print(perf_counter() - start)
print(result)

# Реализация с использованием множеств
start = perf_counter()
result2 = []
unique_num = set()
repeated_num = set()
for num in src:
    if num in repeated_num:
        continue
    if num in unique_num:
        repeated_num.add(num)
        unique_num.discard(num)
        result2.remove(num)
        continue
    result2.append(num)
    unique_num.add(num)
print(perf_counter() - start)
print(result2)