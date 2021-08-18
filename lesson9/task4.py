class Car:
    def __init__(self, speed, color, name, is_police=False):
        self.speed = speed
        self.color = color
        self.name = name
        self.is_police = is_police

    def go(self):
        print('Машина поехала')

    def stop(self):
        print('Машина остановилась')

    def turn(self, direction):
        print(f'Машина повернула на{direction}')

    def show_speed(self):
        print(self.speed)


class TownCar(Car):
    def show_speed(self):
        if self.speed > 60:
            print(f'{self.speed} > 60: Превышение скорости')
        else:
            print(self.speed)

    def car_type(self):
        print('Городская машина')


class WorkCar(Car):
    def show_speed(self):
        if self.speed > 40:
            print(f'{self.speed} > 40: Превышение скорости')
        else:
            print(self.speed)

    def car_type(self):
        print('Рабочая машина')


class SportCar(Car):
    def car_type(self):
        print('Спортивная машина')


class PoliceCar(Car):
    def car_type(self):
        print('Полицейская машина')


rand_car = Car(60, 'Green', 'Lexus')
town = TownCar(80, 'Red', 'Mazda')
work = WorkCar(45, 'Blue', 'КАМАЗ')
police = PoliceCar(90, 'Black', 'BMW', True)
sport = SportCar(120, 'White', 'Porsche')

print(vars(rand_car))
rand_car.go()
rand_car.turn('право')
rand_car.stop()
rand_car.show_speed()
print()

print(vars(town))
town.car_type()
town.go()
town.turn('лево')
town.stop()
town.show_speed()
print()

print(vars(work))
work.car_type()
work.go()
work.turn('право')
work.stop()
work.show_speed()
print()

print(vars(police))
police.car_type()
police.go()
police.turn('лево')
police.stop()
police.show_speed()
print()

print(vars(sport))
sport.car_type()
sport.go()
sport.turn('право')
sport.stop()
sport.show_speed()
