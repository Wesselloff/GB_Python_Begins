#!/usr/bin/python3

#  5. Создать (программно) текстовый файл, записать в него программно набор чисел, разделенных пробелами.
#  Программа должна подсчитывать сумму чисел в файле и выводить ее на экран.


from random import randint
from sys import argv

n = randint(1, 100)
filename = argv[1] if len(argv) > 1 else 'ex05.txt'
with open(filename, 'w', encoding='utf-8') as file:
    for i in range(n):
        file.write(str(randint(-1000, 1000)) + ' ')

with open(filename, 'r', encoding='utf-8') as file:
    print(f'Сумма чисел из файла равна {sum(map(int, file.readline().split()))}')
