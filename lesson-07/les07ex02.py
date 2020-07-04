#!/usr/bin/python3

# 2. Реализовать проект расчета суммарного расхода ткани на производство одежды.
#    Основная сущность (класс) этого проекта — одежда, которая может иметь определенное название.
#    К типам одежды в этом проекте относятся пальто и костюм. У этих типов одежды существуют параметры:
#    размер (для пальто) и рост (для костюма). Это могут быть обычные числа: V и H, соответственно.
#    Для определения расхода ткани по каждому типу одежды использовать формулы:
#    для пальто (V/6.5 + 0.5), для костюма (2 * H + 0.3). Проверить работу этих методов на реальных данных.
#    Реализовать общий подсчет расхода ткани. Проверить на практике полученные на этом уроке знания:
#    реализовать абстрактные классы для основных классов проекта, проверить на практике работу декоратора @property.

from abc import ABC, abstractmethod

class Clothes(ABC):
    def __init__(self, size):
        self.size = size

    @abstractmethod
    def calc(self):
        pass

    def __add__(self, other):
        return self.calc + other.calc


class Coat(Clothes):
    @property
    def calc(self):
        cloth = round(self.size / 6.5, 2) + 0.5
        print(f'Расход ткани на пальто - {cloth}')
        return cloth


class Suit(Clothes):
    @property
    def calc(self):
        cloth = 2 * self.size + 0.3
        print(f'Расход ткани на костюм - {cloth}')
        return cloth


coat = Coat(56)
suit = Suit(185)
print(coat.calc)
print(suit.calc)
print('Общий расход ткани', coat + suit)


