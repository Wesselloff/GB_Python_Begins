#!/usr/bin/python3

# 2. Реализовать класс Road (дорога), в котором определить атрибуты: length (длина), width (ширина).
#    Значения данных атрибутов должны передаваться при создании экземпляра класса. Атрибуты сделать защищенными.
#    Определить метод расчета массы асфальта, необходимого для покрытия всего дорожного полотна.
#    Использовать формулу: длина * ширина * масса асфальта для покрытия одного кв метра дороги асфальтом,
#    толщиной в 1 см * число см толщины полотна. Проверить работу метода.
#    Например: 20м * 5000м * 25кг * 5см = 12500 т


class Road:
    mass1cm = 25
    height = 5

    def __init__(self, length, width):
        self._length = length
        self._width = width

    def full_mass(self):
        try:
            return f'Полная масса полотна асфальта равна ' \
                   f'{float(self._length) * float(self._width) * self.height * self.mass1cm / 1000} тонн'
        except ValueError:
            return 'Ошибка входных данных - допустимы только числа'


length, width = input('Введите длину и ширину дороги: ').split()
road = Road(length, width)
print(road.full_mass())
