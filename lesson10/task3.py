class Cell:
    def __init__(self, numb):
        try:
            self.numb = int(numb)
        except ValueError:
            print('None')
            self.numb = None

    def __str__(self):
        return str(self.numb)

    def __add__(self, other):
        return Cell(self.numb + other.numb)

    def __sub__(self, other):
        if self.numb > other.numb:
            return Cell(self.numb - other.numb)
        else:
            print('Вычитание невозможно')

    def __mul__(self, other):
        return Cell(self.numb * other.numb)

    def __floordiv__(self, other):
        return Cell(self.numb // other.numb)

    def make_order(self, row):
        result = ''
        for el in range(self.numb):
            if el % row == 0 and el != 0:
                result += '\n'
            result += '*'
        return result


my_cell_1 = Cell(30)
my_cell_2 = Cell(5)
my_cell_3 = Cell(8)
print(my_cell_1 + my_cell_2)
print(my_cell_1 - my_cell_2)
print(my_cell_1 * my_cell_2)
print(my_cell_1 // my_cell_2)
print(my_cell_1.make_order(7))
