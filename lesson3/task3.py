def thesaurus(*name_list):
    diction = {}
    my_list = []
    name_list = sorted(name_list)
    for el in name_list:
        for el1 in name_list:
            if el[0] == el1[0]:
                my_list.append(el1)
        diction.update({el[0]: my_list[:]})
        my_list.clear()
    return diction


print(thesaurus('Михаил', 'Павел', 'Алексей', 'Пётр', 'Александр', 'Антон'))
