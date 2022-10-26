# Условие задачи: На столе лежит 2021 конфета. Играют два игрока делая ход друг после друга.
# Первый ход определяется жеребьёвкой. За один ход можно забрать не более чем 28 конфет.
# Все конфеты оппонента достаются сделавшему последний ход. Сколько конфет нужно взять первому игроку, ч
# тобы забрать все конфеты у своего конкурента?
# a) Добавьте игру против бота
# b) * Подумайте как наделить бота ""интеллектом""

# В этой игре  только одна выигрышная стратегия - брать колличество конфет 
# равное остатку от деления кол-ва конфет на макс.возможное за раз + 1шт

import random

candys = 201
max_stp = 28
pl = 0

# выбор с кем будем играть
print('Кто будет вторым игроком?\n выберите цифру:\n компьютер - 1\n человек - 2')

while pl not in range(1, 3):
    pl = input()
    try:
        pl = int(pl)
    except:
        print("Некорректный ввод. Вы уверены, что ввели число?")
        continue
if pl == 1:
    ai = True
else:
    ai = False

# Жеребьевка очередности
input('Для жеребьевки нажмите ENTER')
if random.choice([True, False]):
    order = (1, 2)
else:
    order = (2, 1)

print(f'Первым берет конфеты игрок {order[0]}')
print(f'За один ход можно забрать не более чем {max_stp} конфет')
print(f'Всего конфет: {candys}')


def step(candys):
    """
    Ввод колличества  от пользователя с проверкой ввода
    """
    player_step = 0
    while player_step not in range(1, max_stp+1):
        player_step = input()
        try:
            player_step = int(player_step)
        except:
            print("Некорректный ввод. Вы уверены, что ввели число?")
            continue
        if player_step > candys:
            print('вы хотите взять конфет больше, чем осталось')
            player_step = 0
    return player_step


def stepAI(candys):
    """
    Функция расчета хода компьютера по формуле выигрыша
    """
    player_step = candys % (max_stp+1)
    return player_step


# Игровой процесс
choice = 0
while candys > 0:
    for player_num in order:
        if player_num == 1:
            print('Первый игрок, ваш ход:')
        else:
            print('Второй игрок, ваш ход:')
        if ai and player_num == 2:
            choice = stepAI(candys)
        else:
            choice = step(candys)
        candys -= choice
        print(f'игрок взял {choice} конф., осталось {candys}')
        if candys == 0:
            break

# Вывод результата
print(f'Победил игрок {player_num}')
