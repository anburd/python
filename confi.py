# Условие задачи: На столе лежит 2021 конфета. Играют два игрока делая ход друг после друга. 
# Первый ход определяется жеребьёвкой. За один ход можно забрать не более чем 28 конфет. 
# Все конфеты оппонента достаются сделавшему последний ход. Сколько конфет нужно взять первому игроку, ч
# тобы забрать все конфеты у своего конкурента?
# a) Добавьте игру против бота
# b) * Подумайте как наделить бота ""интеллектом""
import random

candys=201
pl2=0
print('Кто будет вторым игроком?\n выберите цифру:\n компьютер - 1\n человек - 2')

while pl2 not in range(1,3):
    pl2 = input()
    try:
        pl2 = int(pl2)
    except:
        print("Некорректный ввод. Вы уверены, что ввели число?")
        continue
if pl2 == 1: ai=True
else: ai=False


input('Для жеребьевки нажмите ENTER')
if random.choice([True, False]): order=(1, 2) 
else: order=(2, 1)
print(f'Первым берет конфеты игрок {order[0]}')


print('За один ход можно забрать не более чем 28 конфет')

print(f'Всего конфет: {candys}')

def step(candys):
    player_step = 0
    while player_step not in range(1,29):
        player_step1 = input()
        try:
            player_step = int(player_step)
        except:
            print("Некорректный ввод. Вы уверены, что ввели число?")
            continue
        if player_step > candys: 
            print ('вы хотите взять конфет больше, чем осталось')
            player_step = 0
    return player_step 

def stepAI(candys):
    player_step = candys%29
    return player_step

choice=0
while candys > 0:
    for player_num in order:
        if player_num==1:    
            print('Первый игрок, ваш ход:')    
        else:
            print('Второй игрок, ваш ход:')    
        if ai and player_num==2: choice=stepAI(candys)    
        else: choice=step(candys)
        candys -= choice   
        print(f'игрок взял {choice} конф., осталось {candys}')
        if candys==0: break
 

print(f'Победил игрок {player_num}')


