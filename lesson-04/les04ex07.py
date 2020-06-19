#!/usr/bin/python3

# 7. Реализовать генератор с помощью функции с ключевым словом yield, создающим очередное значение.
#    При вызове функции должен создаваться объект-генератор. Функция должна вызываться следующим образом:
#    for el in fact(n). Функция отвечает за получение факториала числа, а в цикле необходимо выводить только
#    первые n чисел, начиная с 1! и до n!.
#    Подсказка: факториал числа n — произведение чисел от 1 до n. Например, факториал четырёх 4! = 1 * 2 * 3 * 4 = 24.


def factorial(pn):
    """Рекурсивная функция расчета факториала"""
    return 1 if pn == 0 else factorial(pn - 1) * pn


def fact(pn):
    for i in range(1, pn):
        yield factorial(i)


while True:
    try:
        n = int(input('Введите целое положительное число: '))
        if n <= 0:
            print('Ошибка ввода. ', end=' ')
        else:
            break
    except ValueError:
        print('Вы ввели не число. ', end=' ')
print([el for el in fact(n)])
