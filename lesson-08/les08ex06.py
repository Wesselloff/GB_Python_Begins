#!/usr/bin/python3

# 6. Продолжить работу над вторым заданием. Реализуйте механизм валидации вводимых пользователем данных.
#    Например, для указания количества принтеров, отправленных на склад, нельзя использовать строковый тип данных.
#    Подсказка: постарайтесь по возможности реализовать в проекте «Склад оргтехники» максимум возможностей,
#    изученных на уроках по ООП.


class EquipmentNotFound(Exception):
    def __init__(self, txt):
        self.txt = txt


class Warehouse:
    def __init__(self):
        self.equipments = []

    def __str__(self):
        return ''.join([str(i) + '\n' for i in self.equipments])

    def to_store(self, equip):
        """Помещение оборудования на склад, как нового, так и переданного ранее в другое подразделение"""
        is_new = True
        for i in self.equipments:
            if i == equip:
                is_new = False
                i.location = 'Store'
                print(f'Оборудование {equip} возвращено на склад')
                break
        if is_new:
            equip.location = 'Store'
            self.equipments.append(equip)
            print(f'Оборудование {equip} помещено на склад')

    def to_location(self, equip, location):
        """
           Передача оборудования со склада в другое подразделение.
           При попытке передать несуществующее оборудование возвращается сообщение об ошибке
        """
        found = False
        for i in self.equipments:
            if i == equip:
                found = True
                i.location = location
                print(f'Оборудование {equip} передано подразделению "{location}"')
                break
        if not found:
            raise EquipmentNotFound(f'Оборудование {equip} на складе не числится')

    def write_off(self, equip):
        """Списание оборудования со склада"""
        try:
            self.equipments.remove(equip)
            print(f'Оборудование {equip} списано со склада')
        except ValueError:
            raise EquipmentNotFound(f'Оборудование {equip} на складе не числится')

    @property
    def on_store(self):
        """Количество единиц офисной техники, хранящейся на складе"""
        return len([i for i in self.equipments if i.location == 'Store'])

    @property
    def in_use(self):
        """Количество единиц офисной техники, переданной пользователям"""
        return len([i for i in self.equipments if i.location != 'Store'])

class OfficeEquipment:
    def __init__(self, model, serial_num):
        self.model = model
        self.serial_num = serial_num
        self.location = ''

    def __str__(self):
        return f'{self.__class__.__name__} {self.model} s/n {self.serial_num}'

    def __eq__(self, other):
        return True if self.model == other.model and self.serial_num == other.serial_num else False


class Printer(OfficeEquipment):
    def __init__(self, model, serial_num, print_system, paper_format='A4', duplex=False):
        super().__init__(model, serial_num)
        self.print_system = print_system
        self.paper_format = paper_format
        self.duplex = duplex


class Scanner(OfficeEquipment):
    def __init__(self, model, serial_num, doc_type):
        super().__init__(model, serial_num)
        self.doc_type = doc_type


class Copier(OfficeEquipment):
    def __init__(self, model, serial_num, cpm=0, paper_format='A4'):
        super().__init__(model, serial_num)
        self.cpm = cpm   # Число копий в минуту
        self.paper_format = paper_format


store = Warehouse()
prn1 = Printer('HP', '2345ljndlfk', 'Laser')
store.to_store(prn1)
prn2 = Printer('Canon', 'jdfjg00845ldsfm', 'Струйный')
store.to_store(prn2)
store.to_location(prn1, 'Бухгалтерия')
store.to_store(Scanner('NoName', '123456789', 'Листовой'))
try:
    store.write_off(Copier('Aficio', 'lsdkjf'))
except EquipmentNotFound as eq:
    print(eq)
print(store)
print(f'На складе хранится {store.on_store} единиц оборудования, передано пользователям - {store.in_use}')
