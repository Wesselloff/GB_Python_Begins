#!/usr/bin/python3

# 3. Реализовать программу работы с органическими клетками. Необходимо создать класс Клетка.
#    В его конструкторе инициализировать параметр, соответствующий количеству клеток (целое число).
#    В классе должны быть реализованы методы перегрузки арифметических операторов:
#    сложение (__add__()), вычитание (__sub__()), умножение (__mul__()), деление (__truediv__()).
#    Данные методы должны применяться только к клеткам и выполнять увеличение, уменьшение, умножение и
#    обычное (не целочисленное) деление клеток, соответственно.
#    В методе деления должно осуществляться округление значения до целого числа.


class Cell:
    def __init__(self, cell_num):
        self.cell_num = cell_num

    def make_order(self, rows):
        return '\n'.join(['*' * rows for i in range(self.cell_num // rows)]) + '\n' + '*' * (self.cell_num % rows)

    def __str__(self):
        return str(self.cell_num)

    def __add__(self, other):
        return Cell(self.cell_num + other.cell_num)

    def __sub__(self, other):
        return Cell(self.cell_num - other.cell_num) if self.cell_num > other.cell_num \
            else 'Размер второй клетки не может превышать первую'

    def __mul__(self, other):
        return Cell(self.cell_num * other.cell_num)

    def __truediv__(self, other):
        return Cell(round(self.cell_num / other.cell_num))


c1 = Cell(10)
c2 = Cell(15)
c3 = Cell(8)
print(c1.make_order(3))
print(c1 + c2)
print((c1 + c2).make_order(7))
print(c1 - c2)
print(c1 - c3)
print((c1 * c2 * c3).make_order(55))
print(((c1 + c2) / c3).make_order(2))
print(c2 / c3)
