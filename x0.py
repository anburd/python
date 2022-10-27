# Создайте программу для игры в ""Крестики-нолики"".

# решил не как у всех сделать адреса клеток не цифрами а вида а1 а вместо Х и О  сделал >< и <>, но такк как это символы можно сменитьна что другое

import os
import random

print('Первый игрок ходит первым, вторым игроком может быть человек или компьютер.\n Адрес клетки вводится в виде буквацифра, например b1 (клавиатура в английской расскладке).\n ')

# список адресов игрового простраства
areas = ['a1', 'a2', 'a3', 'b1', 'b2', 'b3', 'c1', 'c2', 'c3']
# задаем переменные
count = 0
smb = ''
pl = 0
smb = ''

# список победных комбинаций адресов 
wins_lst = [[0, 1, 2], [3, 4, 5], [6, 7, 8], [0, 3, 6], [1, 4, 7],
            [2, 5, 8], [0, 4, 8], [2, 4, 6]]

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

# прописываем функции, описания функций добавли в соотв.блок функции

def printGameArea():
    """
    Функция выводит на экран игровое поле
    """
    os.system('cls' if os.name == 'nt' else 'clear')
    for i in range(0, 9, 3):
        print('-' * 16)
        print('|', areas[i], '|', areas[i+1], '|', areas[i+2], '|')
    print('-' * 16)


def move():
    """
    Функция хода игрока - на ввод адреса выдает индекс игрового пространства этого хода
    """
    s = ''
    step = None
    print(f'Игрок {player_num}')
    while s not in areas:
        s = input('ваш ход: ')
    step = areas.index(s)
    return step


def checking(symbol):
    """
    Функция проверки наличия выиграшной комбинации (2 символа в ряд)
    и возможности закончить ряд - выдает индекс свободной клетки для завершения ряда
    """ 
    result = None
    for i in wins_lst:
        free = []
        count = 0
        for j in range(3):
            if areas[i[j]] == symbol:
                count += 1
            if areas[i[j]] != '<>' and areas[i[j]] != '><':
                free.append(i[j])
        if count == 2 and free:
            result = free[0]
    return result


def robot():
    """
    Функция хода компьютера - проводит проверку:
    если свободен центр - занять его
    если у соперника выиграшная комбинация (2 символа в ряд)- помешать
    если у компьютеры выиграшная комбинация - закончить ряд
    если нет ничего вышеописанного - случайный ход в свободную клетку
    и выдает индекс игрового пространства этого хода
    """
    if areas[4] == 'b2':
        step = 4
        return step
    for symbol in ('><', '<>'):
        step = checking(symbol)
        if step != None:
            return step
    freecells = [i for i in range(
        len(areas)) if areas[i] != '><' and areas[i] != '<>']
    step = int(str(random.choices(freecells))[1])
    return step


def check_win(count, winner):
    """
    Функция проверяет наличие победителя или возможность продолжить игру
    """
    win = False
    if count == 9 or winner != 0:
        win = True
    return win


def check_winner():
    """
    Функция проверяет кто победил и выдает номер победителя или 0 если ничья
    """
    winner = 0
    for i in wins_lst:
        if areas[i[0]] == '><' and areas[i[1]] == '><' and areas[i[2]] == '><':
            winner = 1
        if areas[i[0]] == '<>' and areas[i[1]] == '<>' and areas[i[2]] == '<>':
            winner = 2
    return winner

# Начало игрового процесса
printGameArea()

check = False
while count < 9:
    if check == True:
        break
    for player_num in (1, 2):
        check = check_win(count, check_winner())

        if check == True:
            break
        if player_num == 1:
            smb = '><'
        else:
            smb = '<>'
        if ai and player_num == 2:
            areas[robot()] = smb
        else:
            areas[move()] = smb
        printGameArea()
        count += 1

# Вывод результата
print('game over')

res = check_winner()
print()

if res == 0:
    print('Победила дружба! Ничья')
elif res == 1:
    print('Победил первый игрок')
elif res == 2 and ai:
    print('Победил компьютер.')
else:
    print('Победил второй игрок')
