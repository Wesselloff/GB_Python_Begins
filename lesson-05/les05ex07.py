#!/usr/bin/python3

# 7. Создать (не программно) текстовый файл, в котором каждая строка должна содержать данные о фирме:
#    название, форма собственности, выручка, издержки.
#    Пример строки файла: firm_1 ООО 10000 5000.
#    Необходимо построчно прочитать файл, вычислить прибыль каждой компании, а также среднюю прибыль.
#    Если фирма получила убытки, в расчет средней прибыли ее не включать.
#    Далее реализовать список. Он должен содержать словарь с фирмами и их прибылями, а также словарь
#    со средней прибылью. Если фирма получила убытки, также добавить ее в словарь (со значением убытков).
#    Пример списка: [{“firm_1”: 5000, “firm_2”: 3000, “firm_3”: 1000}, {“average_profit”: 2000}].
#    Итоговый список сохранить в виде json-объекта в соответствующий файл.
#    Пример json-объекта:
#    [{"firm_1": 5000, "firm_2": 3000, "firm_3": 1000}, {"average_profit": 2000}]
#    Подсказка: использовать менеджеры контекста.


from sys import argv
import json

filename = argv[1] if len(argv) > 1 else 'text_7.txt'
try:
    with open(filename, 'r', encoding='utf-8') as file:
        firms = [i.split() for i in file]
except FileNotFoundError:
    print(f'Файл "{filename}" не найден!')
    exit(1)

profits = dict([(i[0], int(i[2]) - int(i[3])) for i in firms])
s = 0
cnt = 0
for i in profits:
    if profits[i] > 0:
        cnt += 1
        s += profits[i]
firmstat = [profits, {'average_profit': round(s / cnt, 2) if cnt > 0 else 0}]
with open('les05ex07.json', 'w', encoding='utf-8') as file:
    json.dump(firmstat, file, ensure_ascii=False, indent=4)
