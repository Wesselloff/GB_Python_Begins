#!/usr/bin/python3

# 3. Реализовать базовый класс Worker (работник), в котором определить атрибуты:
#    name, surname, position (должность), income (доход).
#    Последний атрибут должен быть защищенным и ссылаться на словарь, содержащий элементы: оклад и премия,
#    например, {"wage": wage, "bonus": bonus}.
#    Создать класс Position (должность) на базе класса Worker. В классе Position реализовать методы получения
#    полного имени сотрудника (get_full_name) и дохода с учетом премии (get_total_income).
#    Проверить работу примера на реальных данных (создать экземпляры класса Position, передать данные,
#    проверить значения атрибутов, вызвать методы экземпляров).


class Worker:
    def __init__(self, name, surname, position, rate, bonus):
        self.name = name
        self.surname = surname
        self.position = position
        self._income = {'rate': rate, 'bonus': bonus}


class Position(Worker):
    def get_full_name(self):
        return f'{self.surname} {self.name}'

    def get_total_income(self):
        try:
            return sum(self._income.values())
        except TypeError:
            return 'Некорректные данные по доходам сотрудника'


Vasya = Position('Вася', 'Пупкин', 'Отвечающий за всё', 10000, 5000)
#Vasya = Position('Вася', 'Пупкин', 'Отвечающий за всё', 'lskdjf', 5000)
print('Полное имя', Vasya.get_full_name())
print('Должность', Vasya.position)
print('Доход', Vasya.get_total_income())
