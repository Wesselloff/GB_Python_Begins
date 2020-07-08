#!/usr/bin/python3

# 4. Начните работу над проектом «Склад оргтехники». Создайте класс, описывающий склад. А также класс «Оргтехника»,
#    который будет базовым для классов-наследников. Эти классы — конкретные типы оргтехники (принтер, сканер, ксерокс).
#    В базовом классе определить параметры, общие для приведенных типов. В классах-наследниках реализовать параметры,
#    уникальные для каждого типа оргтехники.


class Warehouse:
    def __init__(self):
        self.equipments = []

    def to_store(self, equip):
        pass

    def to_location(self, equip, location):
        pass

    def write_off(self, equip):
        pass


class OfficeEquipment:
    def __init__(self, model, serial_num):
        self.model = model
        self.serial_num = serial_num
        self.location = ''


class Printer(OfficeEquipment):
    def __init__(self, model, serial_num, print_system, paper_format='A4', duplex=False):
        super().__init__(model, serial_num)
        self.print_system = print_system
        self.paper_format = paper_format
        self.duplex = duplex

    def __str__(self):
        pass


class Scanner(OfficeEquipment):
    def __init__(self, model, serial_num, doc_type):
        super().__init__(model, serial_num)
        self.doc_type = doc_type


class Copier(OfficeEquipment):
    def __init__(self, model, serial_num, cpm=0, paper_format='A4'):
        super().__init__(model, serial_num)
        self.cpm = cpm   # Число копий в минуту
        self.paper_format = paper_format



