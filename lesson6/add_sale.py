from sys import argv

with open("bakery.csv", "a+", encoding="utf-8") as f:
    if len(argv) > 1:
        print(argv[1], file=f)
