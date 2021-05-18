class Complex:
    def __init__(self, numb):
        self.numb = numb

    def __add__(self, other):
        if self.numb.count('+'):
            num_1 = self.numb.split('+')
        else:
            num_1 = self.numb.split('-')
            if len(num_1) > 2:
                num_1.remove('')
                num_1[0] = '-' + num_1[0]
            num_1[1] = '-' + num_1[1]
        if other.numb.count('+'):
            num_2 = other.numb.split('+')
        else:
            num_2 = other.numb.split('-')
            if len(num_2) > 2:
                num_2.remove('')
                num_2[0] = '-' + num_2[0]
                print(num_2[0])
            num_2[1] = '-' + num_2[1]

        num_1[1] = num_1[1].removesuffix('j')
        num_2[1] = num_2[1].removesuffix('j')
        result_real = int(num_1[0]) + int(num_2[0])
        result_img = int(num_1[1]) + int(num_2[1])

        if result_img < 0:
            result = f'{result_real}{result_img}j'
        else:
            result = f'{result_real}+{result_img}j'
        return result

    def __mul__(self, other):
        if self.numb.count('+'):
            num_1 = self.numb.split('+')
        else:
            num_1 = self.numb.split('-')
            if len(num_1) > 2:
                num_1.remove('')
                num_1[0] = '-' + num_1[0]
            num_1[1] = '-' + num_1[1]
        if other.numb.count('+'):
            num_2 = other.numb.split('+')
        else:
            num_2 = other.numb.split('-')
            if len(num_2) > 2:
                num_2.remove('')
                num_2[0] = '-' + num_2[0]
                print(num_2[0])
            num_2[1] = '-' + num_2[1]

        num_1[1] = num_1[1].removesuffix('j')
        num_2[1] = num_2[1].removesuffix('j')
        result_real = (int(num_1[0]) * int(num_2[0])) - (int(num_1[1]) * int(num_2[1]))
        result_img = (int(num_1[0]) * int(num_2[1])) + (int(num_2[0]) * int(num_1[1]))

        if result_img < 0:
            result = f'{result_real}{result_img}j'
        else:
            result = f'{result_real}+{result_img}j'
        return result


my_num_1 = Complex('5-6j')
my_num_2 = Complex('-3+2j')
print(my_num_1 + my_num_2)
print(my_num_1 * my_num_2)
