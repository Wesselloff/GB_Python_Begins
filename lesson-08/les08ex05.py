#!/usr/bin/python3

# 5. Продолжить работу над первым заданием. Разработать методы, отвечающие за приём оргтехники на склад и
#    передачу в определенное подразделение компании. Для хранения данных о наименовании и количестве единиц оргтехники,
#    а также других данных, можно использовать любую подходящую структуру, например словарь.


class Warehouse:
    def __init__(self):
        self.equipments = []

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
            print(f'Оборудование {equip} на складе не числится')

    def write_off(self, equip):
        """Списание оборудования со склада"""
        try:
            self.equipments.remove(equip)
            print(f'Оборудование {equip} списано со склада')
        except ValueError:
            print(f'Оборудование {equip} на складе не числится')


class OfficeEquipment:
    def __init__(self, model, serial_num):
        self.model = model
        self.serial_num = serial_num
        self.location = ''

    def __str__(self):
        return self.model

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
store.write_off(Copier('Aficio', 'lsdkjf'))
