class Warehouse:
    content = {}

    @staticmethod
    def get(name, quantity, where_to):
        exist = False
        if name in Warehouse.content.keys():
            exist = True
            if Warehouse.content[name] >= quantity:
                Warehouse.content[name] -= quantity
                print(f'\n{quantity} штук {name} было перемещено со склада в {where_to}\n')
                if Warehouse.content[name] == 0:
                    Warehouse.content.pop(name)
            else:
                print(f'\nНа складе нет достаточного колличества данной техники. '
                      f'Доступное колличество техники с наименованием {name}: {Warehouse.content[name]}\n')
        if not exist:
            print(f'\nНа складе нет техники с наименованием: {name}\n')

    @staticmethod
    def view_contents():
        text = str(Warehouse.content)
        text = text = text.replace('{', '').replace('}', '\n').replace("'", '')
        print(text) if text.replace('\n', '') else print('\nСклад пуст\n')



class OfficeEquipment:
    def __init__(self):
        self.name = input('Введите название техники: ')

    def warehouse_put(self, quantity):
        already_there = False
        if self.name in Warehouse.content.keys():
            Warehouse.content[self.name] += quantity
            already_there = True
        if not already_there:
            Warehouse.content.update({self.name: quantity})

        print('\nТехника добавлена на склад\n')


class Printer(OfficeEquipment):
    def __init__(self):
        super().__init__()
        self.print_spd = input('Введите скорость печати: ')


class Scanner(OfficeEquipment):
    def __init__(self):
        super().__init__()
        self.scan_res = input('Введите разрешение копирования: ')


class XeroxMachine(OfficeEquipment):
    def __init__(self):
        super().__init__()
        self.copies_per_min = input('Введите скорость копирования в копиях в минуту: ')


if __name__ == '__main__':
    stop = False

    while not stop:
        command = input('1 - показать содержимое склада\n'
                        '2 - добавить технику на склад\n'
                        '3 - отправить технику со склада в подразделение компании\n'
                        '4 - выход из программы\n'
                        '\nВыберите опцию: ')
        if command == '1':
            Warehouse.view_contents()
        elif command == '2':
            try:
                to_add = input('1 - добавить принтер\n'
                               '2 - добавить сканнер\n'
                               '3 - добавить ксерокс\n'
                               '\nВыберите что вы хотите добавть: ')
                if to_add == '1':
                    printer = Printer()
                    eq_quantity = int(input(f'Сколько штук {printer.name} вы хотите добавить? '))
                    printer.warehouse_put(eq_quantity)
                elif to_add == '2':
                    scanner = Scanner()
                    eq_quantity = int(input(f'Сколько штук {scanner.name} вы хотите добавить? '))
                    scanner.warehouse_put(eq_quantity)
                elif to_add == '3':
                    xerox = XeroxMachine()
                    eq_quantity = int(input(f'Сколько штук {xerox.name} вы хотите добавить? '))
                    xerox.warehouse_put(eq_quantity)
                else:
                    print('\nНеверная команда')
                    break
            except ValueError:
                print('\nКолличество должно быть числом\n')
        elif command == '3':
            eq_name = input('Введите наименование техники которую вы хотите отправить: ')
            if eq_name in Warehouse.content.keys():
                eq_quantity = int(input('Введите колличество: '))
                eq_where_to = input('Введите подразделение компании в которе вы хотите отправить данную технику: ')
                Warehouse.get(eq_name, eq_quantity, eq_where_to)
            else:
                print(f"\nНа складе нет техники с наименованием: {eq_name}\n")
        elif command == '4':
            stop = True
        else:
            print('\nНеверная команда')