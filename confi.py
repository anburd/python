# Условие задачи: На столе лежит 2021 конфета. Играют два игрока делая ход друг после друга. 
# Первый ход определяется жеребьёвкой. За один ход можно забрать не более чем 28 конфет. 
# Все конфеты оппонента достаются сделавшему последний ход. Сколько конфет нужно взять первому игроку, ч
# тобы забрать все конфеты у своего конкурента?
# a) Добавьте игру против бота
# b) * Подумайте как наделить бота ""интеллектом""


candys=201



print('За один ход можно забрать не более чем 28 конфет')

print(candys)

def step(candys):
    player_step = 0
    while player_step not in range(1,29):
        player_step = input()
        try:
            player_step = int(player_step)
        except:
            print("Некорректный ввод. Вы уверены, что ввели число?")
            continue
        if player_step > candys: 
            print ('вы хотите взять конфет больше, чем осталось')
            player_step = 0
    return player_step 

player_num=1

def stepAI(candys):
    player_step = candys%29
    return player_step

# step2=step
step2=stepAI

while candys > 0:
    if player_num==1:    
        print('Первый игрок, ваш ход:')    
        candys-=step(candys)    
        print(candys)
        if candys==0: break
        player_num=2
    if player_num==2:    
        print('Второй игрок, ваш ход:')    
        candys-=step2(candys)    
        print(candys)
        if candys==0: break
        player_num=1    

print(player_num)

# print(candys/29)
# print(candys//29)
# print(candys%29)

