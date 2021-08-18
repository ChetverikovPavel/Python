from sys import argv

with open("bakery.csv", "r", encoding="utf-8") as f:
    if len(argv) == 3:
        content = f.read().splitlines()
        for el in content[int(argv[1]) - 1:int(argv[2])]:
            print(el)
    elif len(argv) == 2:
        content = f.read().splitlines()
        for el in content[int(argv[1]) - 1:]:
            print(el)
    else:
        for el in f:
            print(el, end='')
