#!/usr/bin/python3

# 1. Реализовать класс «Дата», функция-конструктор которого должна принимать дату в виде строки формата
# «день-месяц-год». В рамках класса реализовать два метода. Первый, с декоратором @classmethod, должен извлекать число,
# месяц, год и преобразовывать их тип к типу «Число». Второй, с декоратором @staticmethod, должен проводить валидацию
# числа, месяца и года (например, месяц — от 1 до 12). Проверить работу полученной структуры на реальных данных.


class Date:
    d = 0
    m = 0
    y = 0

    def __init__(self, strdate):
        Date.decode(strdate)

    def __str__(self):
        return f'{self.d:02}.{self.m:02}.{self.y}' if Date.validate(self) else 'Некорректный формат даты'

    @classmethod
    def decode(cls, strdate):
        cls.d, cls.m, cls.y = list(map(int, strdate.split('-')))

    @staticmethod
    def validate(self):
        if self.m > 12 or self.d > 31 or self.y > 3000 or self.y < 1000:
            return False
        if self.m in [4, 6, 9, 11] and self.d > 30:
            return False
        if self.m == 2 and self.d > 28 and self.y % 4 != 0:
            return False
        if self.m == 2 and self.d > 29 and self.y % 4 == 0:
            return False
        return True


sd1 = Date('07-11-1917')
print(sd1)

sd2 = Date('31-06-2020')
print(sd2)
