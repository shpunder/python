# Задача - 1
# Ранее мы с вами уже писали игру, используя словари в качестве
# структур данных для нашего игрока и врага, давайте сделаем новую, но уже с ООП
# Опишите базовый класс Person, подумайте какие общие данные есть и у врага и у игрока
# Не забудьте, что у них есть помимо общих аттрибутов и общие методы.
# Теперь наследуясь от Person создайте 2 класса Player, Enemy.
# У каждой сущности должы быть аттрибуты health, damage, armor
# У каждой сущности должно быть 2 метода, один для подсчета урона, с учетом брони противника,
# второй для атаки противника.
# Функция подсчета урона должна быть инкапсулирована
# Вам надо описать игровой цикл так же через класс.
# Создайте экземпляры классов, проведите бой. Кто будет атаковать первым оставляю на ваше усмотрение.


class Person:

    def __init__(self, name, health, damage, armor):
        self.name = name
        self.health = health
        self.damage = damage
        self.armor = armor
        self._hello()

    def _hello(self):
        print(f'Привет враг. Меня зовут {self.name}')

# т.к. методы одинаковые, то можно и не наследовать, но в задании нужно наследовать
class Player(Person):

    def _calculate_damage(self, armor):
        return self.damage / armor

    def attack(self, enemy):
        return round(self._calculate_damage(enemy.armor), 0)

class Enemy(Person):

    def _calculate_damage(self, armor):
        return self.damage / armor

    def attack(self, player):
        return round(self._calculate_damage(player.armor), 0)




player = Player('Ivan', 100, 50, 2)
enemy = Enemy('Vasya', 120, 40, 3)


i = 0
#  цикл самой игры
while True:
    if i % 2 == 0:  # условие для определения чей ход
        enemy.health -= player.attack(enemy)
    else:
        player.health -= enemy.attack(player)
        # проверка после второго хода, чтобы было равное число ударов у каждого игрок
        if enemy.health <= 0 and player.health <= 0:
            print('Ничья')
            break
        elif enemy.health <= 0:
            print(f'Победил', player.name)
            break
        elif player.health <= 0:
            print(f'Победил', enemy.name)
            break
    i += 1
    print(f'Итог после хода №{i}')
    print(f'У {player.name} осталось жизней {player.health}')
    print(f'У {enemy.name} осталось жизней {enemy.health}')