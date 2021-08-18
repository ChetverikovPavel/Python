from time import perf_counter


class TrafficLight:
    __color = 'Красный'

    def running(self):
        start = 0
        flag = 0
        while True:
            if self.__color == 'Красный':
                print(f'Светофор: {self.__color} цвет')
                start = perf_counter()
                while (perf_counter() - start) < 7:
                    continue
                else:
                    self.__color = 'Желтый'
                    start = perf_counter()
                    flag = 1
            if self.__color == 'Желтый':
                print(f'Светофор: {self.__color} цвет')
                while (perf_counter() - start) < 2:
                    continue
                else:
                    start = perf_counter()
                    if flag == 1:
                        self.__color = 'Зелёный'
                    else:
                        self.__color = 'Красный'
            if self.__color == 'Зелёный':
                print(f'Светофор: {self.__color} цвет')
                while (perf_counter() - start) < 7:
                    continue
                else:
                    self.__color = 'Желтый'
                    start = perf_counter()
                    flag = 0


my_traffic = TrafficLight()
my_traffic.running()
