#!/usr/bin/python3

# 4. Создать (не программно) текстовый файл со следующим содержимым:
#    One — 1
#    Two — 2
#    Three — 3
#    Four — 4
#    Необходимо написать программу, открывающую файл на чтение и считывающую построчно данные.
#    При этом английские числительные должны заменяться на русские.
#    Новый блок строк должен записываться в новый текстовый файл.


from sys import argv
filename = argv[1] if len(argv) > 1 else 'text_4.txt'
try:
    with open(filename, 'r', encoding='utf-8') as file:
        english = [i.split() for i in file]
except FileNotFoundError:
    print(f'Файл "{filename}" не найден!')
    exit(1)

en_ru = {'One': 'Один', 'Two': 'Два', 'Three': 'Три', 'Four': 'Четыре'}
#file.close()
russian = []
for i in english:
    russian.append([en_ru[i[0]]] + i[1:])
with open('text_4_ru.txt', 'w', encoding='utf-8') as file:
    for i in russian:
        file.write(' '.join(i) + '\n')
#file.close()
