#!/usr/bin/python3

# 1. Реализовать скрипт, в котором должна быть предусмотрена функция расчета заработной платы сотрудника.
#    В расчете необходимо использовать формулу: (выработка в часах * ставка в час) + премия.
#    Для выполнения расчета для конкретных значений необходимо запускать скрипт с параметрами.


from sys import argv
from os import path


def salary(hours, rate, bonus):
    try:
        return f'Заработано {float(hours) * float(rate) + float(bonus)}'
    except ValueError:
        return 'Ошибка ввода данных. В качестве параметров допустимы только числа.'


if len(argv) < 4:
    print(f'Формат вызова: {path.basename(argv[0])} <часы> <ставка> <премия>')
else:
    print(salary(argv[1], argv[2], argv[3]))
