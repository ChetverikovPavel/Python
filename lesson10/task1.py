from sys import exit
import copy


class Matrix:
    def __init__(self, matrix):
        for el in matrix:
            if len(el) != len(matrix[0]):  # проверка "являются ли ввёдённые данные матрицей"
                print('Введённый массив данных не матрица')
                exit(1)

        self.matrix = matrix

    def __str__(self):
        result = str()
        for el in self.matrix:
            for el_2 in el:
                result += f'{el_2: <4}'
            result += f'\n'
        return result

    def __add__(self, other):
        result_matrix = copy.deepcopy(self.matrix)
        try:
            for i in range(len(self.matrix)):
                for j in range(len(self.matrix[i])):
                    result_matrix[i][j] = self.matrix[i][j] + other.matrix[i][j]

        except IndexError:
            print('Матрицы разного размера')
        else:
            return Matrix(result_matrix)


my_matrix_1 = Matrix([[3, 2], [8, 4], [7, 8]])
my_matrix_2 = Matrix([[5, 1], [3, 9], [6, 2]])
print(my_matrix_1, my_matrix_2, sep='\n')

my_matrix_3 = (my_matrix_1 + my_matrix_2)
print(my_matrix_3)


my_matrix_4 = Matrix([[11, 19, 28], [15, 39, 1], [55, 76, 11]])
my_matrix_5 = Matrix([[5, 4, 11], [21, 13, 7], [15, 3, 17]])
print(my_matrix_4, my_matrix_5, sep='\n')

my_matrix_6 = (my_matrix_4 + my_matrix_5)
print(my_matrix_6)

test_matrix = Matrix([[1], [1, 1]])  # Для проверки "являются ли ввёдённые данные матрицей"
