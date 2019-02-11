# Задача - 1
# Опишите несколько классов TownCar, SportCar, WorkCar, PoliceCar
# У каждого класса должны быть следующие аттрибуты:
# speed, color, name, is_police - Булево значение.
# А так же несколько методов: go, stop, turn(direction) - которые должны сообщать,
#  о том что машина поехала, остановилась, повернула(куда)


class TownCar:


    def __init__(self):
        self.speed = 60
        self.color = 'red'
        self.name = 'nissan'
        self.is_police = False

    def go(self):
        print(f'{self.name} поехала')


    def stop(self):
        print(f'{self.name} остановилась')


    def turn(self, direction):
        print(f'{self.name} повернула на {direction}')



class SportCar:
    def __init__(self):
        self.speed = 60
        self.color = 'red'
        self.name = 'nissan'
        self.is_police = False

    def go(self):
        print(f'{self.name} поехала')


    def stop(self):
        print(f'{self.name} остановилась')


    def turn(self, direction):
        print(f'{self.name} повернула на {direction}')


class WorkCar:
    def __init__(self):
        self.speed = 40
        self.color = 'blue'
        self.name = 'lada'
        self.is_police = False

    def go(self):
        print(f'{self.name} поехала')

    def stop(self):
        print(f'{self.name} остановилась')

    def turn(self, direction):
        print(f'{self.name} повернула на {direction}')


class PoliceCar:
    def __init__(self):
        self.speed = 800
        self.color = 'silver'
        self.name = 'ford'
        self.is_police = True

    def go(self):
        print(f'{self.name} поехала')

    def stop(self):
        print(f'{self.name} остановилась')

    def turn(self, direction):
        print(f'{self.name} повернула на {direction}')


tc = TownCar()
pc = PoliceCar()

tc.go()
tc.turn('лево')
tc.stop()

pc.go()

# Задача - 2
# Посмотрите на задачу-1 подумайте как выделить общие признаки классов
# в родительский и остальные просто наследовать от него.


class Car:
    def __init__(self):
        self.speed = 60
        self.color = 'red'
        self.name = 'nissan'
        self.is_police = False

    def go(self):
        print(f'{self.name} поехала')

    def stop(self):
        print(f'{self.name} остановилась')

    def turn(self, direction):
        print(f'{self.name} повернула на {direction}')


class PoliceCar2(Car):

    def enable_flash(self):
        print('Включили мигалку')


class SportCar2(Car):

    def roar(self):
        print('РРРРРрррр рычит мотор')


pc2 = PoliceCar2()
pc2.go()
pc2.enable_flash()

sc2 = SportCar2()
sc2.roar()