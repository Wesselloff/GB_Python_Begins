#!/usr/bin/python3

# 6. Необходимо создать (не программно) текстовый файл, где каждая строка описывает учебный предмет и
#    наличие лекционных, практических и лабораторных занятий по этому предмету и их количество.
#    Важно, чтобы для каждого предмета не обязательно были все типы занятий.
#    Сформировать словарь, содержащий название предмета и общее количество занятий по нему. Вывести словарь на экран.
#    Примеры строк файла:
#       Информатика: 100(л) 50(пр) 20(лаб).
#       Физика: 30(л) — 10(лаб)
#       Физкультура: — 30(пр) —

#    Пример словаря:
#       {“Информатика”: 170, “Физика”: 40, “Физкультура”: 30}


from sys import argv
filename = argv[1] if len(argv) > 1 else 'text_6.txt'
try:
    with open(filename, 'r', encoding='utf-8') as file:
        # Превращаем строки файла в словарь вида <Предмет>: <остальной текст>
        disciplines = dict(i.split(':') for i in file)
except FileNotFoundError:
    print(f'Файл "{filename}" не найден!')
    exit(1)
for i in disciplines:
    s = 0
    # Раздракониваем текст на составляющие и суммируем всё числовое
    for j in disciplines[i].split():
        if j != '-':
            s += int(''.join(k for k in j if k.isdigit()))
    disciplines[i] = s
print(disciplines)
