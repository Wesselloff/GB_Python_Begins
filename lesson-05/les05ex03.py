#!/usr/bin/python3

# 3. Создать текстовый файл (не программно), построчно записать фамилии сотрудников и величину их окладов.
#    Определить, кто из сотрудников имеет оклад менее 20 тыс., вывести фамилии этих сотрудников.
#    Выполнить подсчет средней величины дохода сотрудников.

from sys import argv
filename = argv[1] if len(argv) > 1 else 'text_3.txt'
try:
    with open(filename, 'r', encoding='utf-8') as file:
        employers = [i.split() for i in file]
except FileNotFoundError:
    print(f'Файл "{filename}" не найден!')
    exit(1)

print('Сотрудники с окладом менее 20 тыс.:')
print([i[0] for i in employers if float(i[1]) < 20000])
print(f'Средняя величина дохода: {sum([float(i[1]) for i in employers]) / len(employers):.2f}')
