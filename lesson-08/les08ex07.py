#!/usr/bin/python3

# 7. Реализовать проект «Операции с комплексными числами». Создайте класс «Комплексное число»,
#    реализуйте перегрузку методов сложения и умножения комплексных чисел. Проверьте работу проекта,
#    создав экземпляры класса (комплексные числа) и выполнив сложение и умножение созданных экземпляров.
#    Проверьте корректность полученного результата.


class Complex:
    def __init__(self, r, i=0):
        self.r = r
        self.i = i

    def __add__(self, other):
        return Complex(self.r + other.r, self.i + other.i)

    def __mul__(self, other):
        return Complex(self.r * other.r - self.i * other.i, self.i * other.r + self.r * other.i)

    def __str__(self):
        if self.r == 0 and self.i != 0:
            return f'{self.i}i'
        else:
            return f'{self.r}{f"{self.i:+}i" if self.i != 0 else ""}'


x = Complex(1, 2)
y = Complex(3, -4)
print(x)
print(y)
print(x + y)
print(x * y)
x += Complex(-2, 3)
print(x)
x *= Complex(2)
print(x)
print(x + Complex(5, -10))
print(Complex(0))
print(Complex(0, 5))
print(Complex(0, -7))
