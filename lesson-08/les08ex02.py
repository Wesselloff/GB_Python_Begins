#!/usr/bin/python3

# 2. Создайте собственный класс-исключение, обрабатывающий ситуацию деления на нуль.
#    Проверьте его работу на данных, вводимых пользователем. При вводе пользователем нуля в качестве делителя
#    программа должна корректно обработать эту ситуацию и не завершиться с ошибкой.


class Div0(Exception):
    def __init__(self, txt):
        self.txt = txt


try:
    a = float(input('Введите делимое: '))
    b = float(input('Введите делитель: '))
    if b == 0:
        raise Div0('Делитель не может быть равен нулю!')
except ValueError:
    print('Вы ввели не число!')
except Div0 as d0:
    print(d0)
else:
    print('Частное равно:', a / b)
