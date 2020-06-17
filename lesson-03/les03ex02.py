# 2. Реализовать функцию, принимающую несколько параметров, описывающих данные пользователя:
#    имя, фамилия, год рождения, город проживания, email, телефон. Функция должна принимать параметры
#    как именованные аргументы. Реализовать вывод данных о пользователе одной строкой.


def user_attr(pname, psurname, pbirthyear, pcity, pemail, pphone):
    print(f'{psurname} {pname}, год рождения {pbirthyear}, проживает в городе {pcity}, контакты: {pemail}, {pphone}')


name = input('Введите имя: ')
surname = input('Введите фамилию: ')
birthyear = input('Введите год рождения: ')
city = input('Введите город: ')
email = input('введите e-mail: ')
phone = input('Введите телефон: ')

user_attr(pname=name, psurname=surname, pbirthyear=birthyear, pcity=city, pemail=email, pphone=phone)
