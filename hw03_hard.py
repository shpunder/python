# Задание - 1
# Давайте опишем пару сущностей player и enemy через словарь,
# который будет иметь ключи и значения:
# name - строка полученная от пользователя,
# health - 100,
# damage - 50.
# Поэксперементируйте с значениями урона и жизней по желанию.
# Теперь надо создать функцию attack(person1, person2), аргументы можете указать свои,
# функция в качестве аргумента будет принимать атакующего и атакуемого,
# функция должна получить параметр damage атакующего и отнять это количество
# health от атакуемого. Функция должна сама работать с словарями и изменять их значения.

import os.path


player = {}
enemy = {}


def split_line(item):
    """функция разбиения строки на список элементов"""
    return item.split(' : ')


def save_file(p):
    """Если такого игрока еще нет, то занесем его в файл"""
    with open(p['name'] + '.txt', 'w+', encoding='utf-8') as file:
        for key in p:
            file.write(f'{key} : {p[key]}\n')


def read_file(name):
    """Если игрок уже есть, то считаем его параметры"""
    with open(name + '.txt', 'r', encoding='utf-8') as file:
        dict_p = {}
        for line in file.readlines():
            list_p = split_line(line.strip())
            if len(dict_p) < 1:  # первый параметр строковый, остальные float
                dict_p[list_p[0]] = list_p[1]
            else:
                dict_p[list_p[0]] = float(list_p[1])
        print(dict_p)
    return dict_p


player_name = input('Введите имя первого игрока: ')
if os.path.exists(player_name + '.txt'):
    print('Такой игрок уже существует. Будут загружены Ваши настройки')
    player = read_file(player_name)
else:
    player = {'name': player_name, 'health': 100, 'damage': 50, 'armor': 1.2}
    save_file(player)


enemy_name = input('Введите имя второго игрока: ')
if os.path.exists(enemy_name + '.txt'):
    print('Такой игрок уже существует. Будут загружены Ваши настройки')
    enemy = read_file(enemy_name)
else:
    enemy = {'name': enemy_name, 'health': 120, 'damage': 4, 'armor': 20}
    save_file(player)


def attack(person1, person2):
    """Нанесение урона с учетом брони в одной функции"""
    person2['health'] -= round(person1['damage'] / person2['armor'], 2)


i = 0
#  цикл самой игры
while True:
    if i % 2 == 0:  # условие для определения чей ход
        attack(player, enemy)
    else:
        attack(enemy, player)
        # проверка после второго хода, чтобы было равное число ударов у каждого игрок
        if enemy['health'] <= 0 and player['health'] <= 0:
            print('Ничья')
            break
        elif enemy['health'] <= 0:
            print(f'Победил', player['name'])
            break
        elif player['health'] <= 0:
            print(f'Победил', enemy['name'])
            break
    i += 1
    print(f'Итог после хода №{i}')
    print(player)
    print(enemy)


# Задание - 2
# Давайте усложним предыдущее задание, измените сущности, добавив новый параметр - armor = 1.2
# Теперь надо добавить функцию, которая будет вычислять и возвращать полученный урон по формуле damage / armor
# Следовательно у вас должно быть 2 функции, одна наносит урон, вторая вычисляет урон по отношению к броне.
# Сохраните эти сущности, полностью, каждую в свой файл,
# в качестве названия для файла использовать name, расширение .txt
# Напишите функцию, которая будет считывать файл игрока и его врага, получать оттуда данные, и записывать их в словари,
# после чего происходит запуск игровой сессии, где сущностям поочередно наносится урон,
# пока у одного из них health не станет меньше или равен 0.
# После чего на экран должно быть выведено имя победителя, и количество оставшихся единиц здоровья.