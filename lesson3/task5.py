import random


def get_jokes(count, flag):
    joke_list = []
    nouns = ["автомобиль", "лес", "огонь", "город", "дом"]
    adverbs = ["сегодня", "вчера", "завтра", "позавчера", "ночью"]
    adjectives = ["веселый", "яркий", "зеленый", "утопичный", "мягкий"]
    i = 0
    flag_2 = 0
    if count > 5 and flag:
        count = 5
        flag_2 = 1
    while count:

        joke_list.append(random.choice(nouns))
        joke_list.append(random.choice(adverbs))
        joke_list.append(random.choice(adjectives))
        if flag:
            nouns.remove(joke_list[i])
            adverbs.remove((joke_list[i + 1]))
            adjectives.remove((joke_list[i + 2]))
        joke_list[i] = ' '.join(joke_list[i:i + 3])
        joke_list.pop()
        joke_list.pop()

        i += 1
        count -= 1
    if flag_2:
        return joke_list, 'Шутки кончились'
    else:
        return joke_list


print(get_jokes(4, 0))  # Запрет повторений слов выключен
print(get_jokes(4, 1))  # Запрет повторений слов включён
print(get_jokes(8, 1))  # Запрет повторений слов включён + шуток больше чем слов
