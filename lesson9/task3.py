class Worker:
    def __init__(self, name, surname, position, income):
        self.name = name
        self.surname = surname
        self.position = position
        self._income = income


class Position(Worker):
    def get_full_name(self):
        return self.surname + ' ' + self.name

    def get_total_income(self):
        return self._income['wage'] + self._income['bonus']


income_1 = {'wage': 40000, 'bonus': 1000}
worker_1 = Position('Иван', 'Иванов', 'Продавец', income_1)
print(vars(worker_1))
print(worker_1.get_full_name())
print(worker_1.get_total_income())
