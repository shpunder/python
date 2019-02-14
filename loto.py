"""
== Лото ==
Правила игры в лото.
Игра ведется с помощью специальных карточек, на которых отмечены числа,
и фишек (бочонков) с цифрами.
Количество бочонков — 90 штук (с цифрами от 1 до 90).
Каждая карточка содержит 3 строки по 9 клеток. В каждой строке по 5 случайных цифр,
расположенных по возрастанию. Все цифры в карточке уникальны. Пример карточки:
--------------------------
    9 43 62          74 90
 2    27    75 78    82
   41 56 63     76      86
--------------------------
В игре 2 игрока: пользователь и компьютер. Каждому в начале выдается
случайная карточка.
Каждый ход выбирается один случайный бочонок и выводится на экран.
Также выводятся карточка игрока и карточка компьютера.
Пользователю предлагается зачеркнуть цифру на карточке или продолжить.
Если игрок выбрал "зачеркнуть":
	Если цифра есть на карточке - она зачеркивается и игра продолжается.
	Если цифры на карточке нет - игрок проигрывает и игра завершается.
Если игрок выбрал "продолжить":
	Если цифра есть на карточке - игрок проигрывает и игра завершается.
	Если цифры на карточке нет - игра продолжается.

Побеждает тот, кто первый закроет все числа на своей карточке.
Пример одного хода:
Новый бочонок: 70 (осталось 76)
------ Ваша карточка -----
 6  7          49    57 58
   14 26     -    78    85
23 33    38    48    71
--------------------------
-- Карточка компьютера ---
 7 11     - 14    87
      16 49    55 77    88
   15 20     -       76  -
--------------------------
Зачеркнуть цифру? (y/n)
Подсказка: каждый следующий случайный бочонок из мешка удобно получать
с помощью функции-генератора.
Подсказка: для работы с псевдослучайными числами удобно использовать
модуль random: http://docs.python.org/3/library/random.html
"""

import random

class Game:

    def __init__(self, name):
        self.card = self.create_card()
        self.name = name

    def create_card(self):
        list_15 = []
        # создам сначала лист с 15 уникальными элементами
        while len(list_15) < 15:
            a = random.randint(1, 90)
            if not a in list_15:
                list_15.append(a)

        # далее 15 разбиваем на три листа и сортируем по возрастанию
        self.card = []
        self.card.append(list_15[0:5])
        self.card[0].sort(key=int)
        self.card.append(list_15[5:10])
        self.card[1].sort(key=int)
        self.card.append(list_15[10:15])
        self.card[2].sort(key=int)
        i = 0
        # далее в случайное место вставляем 4 пробела в каждой строке
        for a in self.card:
            a = a + [' ', ' ', ' ', ' ']
            for _ in range(4):
                a.insert(random.randint(0, 8), ' ')
                a.pop()
            self.card[i] = a
            i += 1
        return self.card

    def show_card(self):
        print(f'------ Карточка игрока {self.name} --------------')
        for a in self.card:
            print(a)
        print('------------------------------------------')

    def chek_card(self):
        sum = 0
        for a in self.card:
            sum += a.count(' ')
            sum += a.count('-')
        return sum == 27 # значит, что закончились цифры в листе


class Player(Game):

    def chek_barrel(self, a):
        print(a)
        while True:
            answer = input('Зачеркнуть цифру? (y/n)').lower()
            if answer == 'y' or answer == 'n':
                break
        for j in range(3):
            for i in self.card[j]:
                if i == a:  # если выбор зачеркнуть и нашли цифру, то все ок, если нет, то конец игры
                    if answer == 'y':
                        self.card[j][self.card[j].index(a)] = '-'
                        return True
                    else:
                        return False
        if answer == 'n':  # если дошли до сюда, то цифру мы не нашли
            return True
        else:
            return False


class Computer(Game):

    def chek_barrel(self, a):
        for j in range(3):
            for i in self.card[j]:
                if i == a:
                    self.card[j][self.card[j].index(a)] = '-'



player = Player('Igor')
computer = Computer('Comp')
used_barrel = []

while True:
    player.show_card()
    computer.show_card()
    while True:
        a = random.randint(1, 90)
        if not a in used_barrel:
            print(used_barrel)
            used_barrel.append(a)
            break
    computer.chek_barrel(a)
    if not player.chek_barrel(a):
        print('Вы проиграли т.к. Ваш выбор не верный!')
        break
    if computer.chek_card() and player.chek_card():
        print(f'Игра окончена. Ничья т.к. последняя цифра была у обоих игроков')
    if computer.chek_card():
        print(f'Игра окончена. Победил {computer.name}')
        break
    if player.chek_card():
        print(f'Игра окончена. Победил игрок {player.name}')
        break
