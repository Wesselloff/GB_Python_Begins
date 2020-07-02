#!/usr/bin/python3

# 5. Реализовать класс Stationery (канцелярская принадлежность).
#    Определить в нем атрибут title (название) и метод draw (отрисовка). Метод выводит сообщение “Запуск отрисовки.”
#    Создать три дочерних класса Pen (ручка), Pencil (карандаш), Handle (маркер).
#    В каждом из классов реализовать переопределение метода draw.
#    Для каждого из классов методы должен выводить уникальное сообщение.
#    Создать экземпляры классов и проверить, что выведет описанный метод для каждого экземпляра.


class Stationery:
    def __init__(self, title='Оно рисует'):
        self.title = title

    def draw(self):
        print(f'Запуск отрисовки - {self.title}')


class Pen(Stationery):
    def draw(self):
        print(f'Рисуем ручкой {self.title}.')


class Pencil(Stationery):
    def draw(self):
        print(f'Рисуем карандашом {self.title}.')


class Handle(Stationery):
    def draw(self):
        print(f'Рисуем маркером {self.title}.')


thing = Stationery()
thing.draw()

pen = Pen('BIC')
pen.draw()

pencil = Pencil('Конструктор')
pencil.draw()

marker = Handle('Permanent')
marker.draw()
