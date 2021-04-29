from sys import exit

with open("users.csv", "r+", encoding="utf-8") as f_1:
    with open("hobby.csv", "r+", encoding="utf-8") as f_2:
        content_1 = f_1.read().splitlines()
        content_2 = f_2.read().splitlines()
        i = 0
        result = dict.fromkeys(content_1)
        if len(content_1) < len(content_2):
            exit(1)
        for el_1 in content_1:
            for el_2 in content_2[i:]:
                result[el_1] = el_2
                i += 1
                break


with open("users_hobby.txt", "r+", encoding="utf-8") as f:
    for el in result:
        print(f"{el}: {result[el]}", file=f)
