#!/usr/bin/python3

#  1. Создать программно файл в текстовом формате, записать в него построчно данные, вводимые пользователем.
#     Об окончании ввода данных свидетельствует пустая строка.

with open('ex01-02.txt', 'w', encoding='utf-8') as file:
    print('Введите текст. Для окончания нажмите "Enter" на пустой строке:')
    while True:
        txt = input()
        if not txt:
            break
        file.write(txt + '\n')