class Stationery:
    def __init__(self, title):
        self.title = title

    def draw(self):
        print('Запуск отрисовки')


class Pen(Stationery):
    def draw(self):
        print('Запуск отрисовки ручкой')


class Pencil(Stationery):
    def draw(self):
        print('Запуск отрисовки карандашом')


class Handle(Stationery):
    def draw(self):
        print('Запуск отрисовки маркером')


rand_st = Stationery('?')
pen = Pen('Parker')
pencil = Pencil('KOH-I-NOOR')
handle = Handle('BRAUBERG')

print(vars(rand_st))
rand_st.draw()
print()

print(vars(pen))
pen.draw()
print()

print(vars(pencil))
pencil.draw()
print()

print(vars(handle))
handle.draw()

