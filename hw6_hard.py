# Задача - 1
# Вам необходимо создать завод по производству мягких игрушек для детей.
# Вам надо продумать структуру классов,
# чтобы у вас был класс, который создает игрушки на основании:
#  Названия, Цвета, Типа (животное, персонаж мультфильма)
# Опишите процедуры создания игрушки в трех методах:
# -- Закупка сырья, пошив, окраска
# Не усложняйте пусть методы просто выводят текст о том, что делают.
# В итоге ваш класс по производству игрушек должен вернуть объект нового класса Игрушка.


class Toy:

    def __init__(self, name, color, material):
        self.name = name
        self.color = color
        self.material = material


class Factory:

    def make(self, name, color, toy_type):
        self._pay(color)
        self._sew()
        self._colouring()
        return Toy(name, color, toy_type)

    def _pay(self, color):
        print('Купили метаериал')

    def _sew(self):
        print('Пошили ткань')

    def _colouring(selfs):
        print('Покрасили игрушку')



toy = Factory()
new_toy = toy.make('Vinny Pooh', 'yellow', 'PlushToy')
print(f'Создали игрушку с именем {new_toy.name}')

# Задача - 2
# Доработайте нашу фабрику, создайте по одному классу на каждый тип, теперь надо в классе фабрика
# исходя из типа игрушки отдавать конкретный объект класса, который наследуется от базового - Игрушка


class Toy:

    def __init__(self, name, color, material):
        self.name = name
        self.color = color
        self.material = material


class PlushToy(Toy):
    def play_music(self):
        print('Нажали кнопку музыка в мягкой игрушке')


class CarToy(Toy):
    def go(self):
        print('Машинка поехала')

class Factory:
    pass

    def make(self, name, color, toy_type):
        self._pay(color)
        self._sew()
        self._colouring()
        if (toy_type == 'Plush'):
            return PlushToy(name, color, toy_type)
        else:
            return CarToy(name, color, toy_type)

    def _pay(self, color):
        print('Купили метаериал')

    def _sew(self):
        print('Пошили ткань')

    def _colouring(selfs):
        print('Покрасили игрушку')



toy = Factory()
new_toy = toy.make('Vinny Pooh', 'yellow', 'Plush')
print(f'Создали игрушку с именем {new_toy.name}')
if (new_toy.material == 'Plush'):
    new_toy.play_music()
else:
    new_toy.go()