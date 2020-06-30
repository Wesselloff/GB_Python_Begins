#!/usr/bin/python3

# 2. Создать текстовый файл (не программно), сохранить в нем несколько строк, выполнить подсчет
#    количества строк, количества слов в каждой строке.

from sys import argv


def rus_ends(n):
    if 5 <= n % 10 <= 9 or 11 <= n <= 19 or n % 10 == 0:
        return f'{n} слов'
    elif n % 10 == 1:
        return f'{n} слово'
    else:
        return f'{n} слова'


filename = argv[1] if len(argv) > 1 else 'ex01-02.txt'
try:
    with open(filename, 'r', encoding='utf-8') as file:
        cnt = 0
        for i in file:
            cnt += 1
            print(f'Строка {cnt} - {rus_ends(len(i.split()))}')
        print(f'Общее число строк в файле - {cnt}')
except FileNotFoundError:
    print(f'Файл "{filename}" не найден!')
    exit(1)
