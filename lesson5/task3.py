def generate(tutors_gen_in_generate, klasses_gen_in_generate):
    for tutor in tutors_gen_in_generate:
        for klass in klasses_gen_in_generate:
            break
        else:
            klass = None
        result = (tutor, klass)
        yield result


tutors = [
    'Иван', 'Анастасия', 'Петр', 'Сергей',
    'Дмитрий', 'Борис', 'Елена', 'Павел', 'Игорь'
]
klasses = [
    '9А', '7В', '9Б', '9В', '8Б', '10А', '10Б', '9А'
]
tutors_gen = (tutor for tutor in tutors)
klasses_gen = (klass for klass in klasses)

print(type(generate(tutors_gen, klasses_gen)))  # Проверка типа
for el in generate(tutors_gen, klasses_gen):  # Цикл работы генератора до истощения
    print(el)
# print(next(generate(tutors_gen, klasses_gen)))  # Проверка истощения генератора, выдаст ошибку