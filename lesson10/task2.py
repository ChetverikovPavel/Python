from abc import ABC, abstractmethod


class Clothes(ABC):
    @abstractmethod
    def calc(self):
        pass


class Overcoat(Clothes):
    def __init__(self, v):
        self.v = v

    @property
    def calc(self):
        return (round(self.v / 6.5 + 0.5, 1))


class Costume(Clothes):
    def __init__(self, h):
        self.h = h

    @property
    def calc(self):
        return (self.h * 2 + 0.3)


my_overcoat = Overcoat(44)
my_costume = Costume(1.80)
print(my_overcoat.calc)
print(my_costume.calc)
