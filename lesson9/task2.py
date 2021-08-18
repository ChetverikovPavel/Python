class Road:
    def __init__(self, length, width):
        self._lenght = length
        self._width = width

    def calculation(self):
        __weight = 25
        __thickness = 5
        __result = self._lenght * self._width * __weight * __thickness // 1000
        print(f'{self._lenght}м * {self._width}м * {__weight}кг * {__thickness}см = {__result}т')


my_road = Road(4000, 15)
my_road.calculation()
