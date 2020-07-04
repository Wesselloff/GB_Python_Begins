#!/usr/bin/python3

# 4. Реализуйте базовый класс Car. У данного класса должны быть следующие атрибуты:
#    speed, color, name, is_police (булево). А также методы: go, stop, turn(direction), которые должны сообщать,
#    что машина поехала, остановилась, повернула (куда).
#    Опишите несколько дочерних классов: TownCar, SportCar, WorkCar, PoliceCar.
#    Добавьте в базовый класс метод show_speed, который должен показывать текущую скорость автомобиля.
#    Для классов TownCar и WorkCar переопределите метод show_speed.
#    При значении скорости свыше 60 (TownCar) и 40 (WorkCar) должно выводиться сообщение о превышении скорости.
#    Создайте экземпляры классов, передайте значения атрибутов. Выполните доступ к атрибутам, выведите результат.
#    Выполните вызов методов и также покажите результат.


class Car:
    def __init__(self, name, color, speed, is_police=False):
        self.name = name
        self.color = color
        self.speed = speed
        self.is_police = is_police
        print(f'Создана машина {self.name}, цвет {self.color}, полицейская - {self.is_police}')

    def go(self):
        print(self.name, 'Поехали!')

    def stop(self):
        print(self.name, 'Остановились.')

    def turn(self, direction):
        print(self.name, f"Поворот {'налево' if direction == 'left' else 'направо'}.")

    def show_speed(self):
        return f'{self.name} едет со скоростью {self.speed}'


class TownCar(Car):
    _max_speed = 60

    def show_speed(self):
        return f'{self.name} скорость {self.speed}.{" Превышение скорости!" if self.speed > self._max_speed else ""}'


class WorkCar(Car):
    _max_speed = 40

    def show_speed(self):
        return f'{self.name} скорость {self.speed}.{" Превышение скорости!" if self.speed > self._max_speed else ""}'


class SportCar(Car):
    pass


class PoliceCar(Car):
    def __init__(self, name, color, speed, is_police=True):
        super().__init__(name, color, speed, is_police)


towncar = TownCar('ЗАЗ', 'в горошек', 30)
towncar.go()
towncar.turn('left')
towncar.turn('right')
print(towncar.show_speed())
towncar.speed = 90
print(towncar.show_speed())
towncar.stop()

police = PoliceCar('Волга', 'черный', 120)
print(police.show_speed())

sport = SportCar('Formula', 'красный', 300)
sport.go()
sport.turn('right')
print(sport.show_speed())

track = WorkCar('Пикап', 'ржавый', 55)
track.go()
print(track.show_speed())
track.speed = 20
print(track.show_speed())
track.stop()
