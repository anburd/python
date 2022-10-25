# Создайте программу для игры в ""Крестики-нолики"".

import os
import random
areas = ['a1', 'a2', 'a3', 'b1', 'b2', 'b3', 'c1', 'c2', 'c3']
count = 0
smb=''
pl=0



smb = ('><')
wins_lst = [[0, 1, 2], [3, 4, 5], [6, 7, 8], [0, 3, 6], [1, 4, 7], 
[2, 5, 8], [0, 4, 8], [2, 4, 6]]
print('Кто будет вторым игроком?\n выберите цифру:\n компьютер - 1\n человек - 2')
while pl not in range(1,3):
    pl = input()
    try:
        pl = int(pl)
    except:
        print("Некорректный ввод. Вы уверены, что ввели число?")
        continue
if pl == 1: ai=True
else: ai=False

def printGameArea():

    os.system('cls' if os.name == 'nt' else 'clear')
    for i in range(0, 9, 3):
        print('----------------')
        print('|', areas[i], '|', areas[i+1], '|', areas[i+2], '|')
    print('----------------')

def move():
    s = ''
    step=None
    print(f'Игрок {player_num}')
    while s not in areas:
        s=input('ваш ход: ')
        step = areas.index(s)
    return step

def checking(symbol):
    result=None
    for i in wins_lst:
        free=[]

        count = 0
        for j in range(3):
            if areas[i[j]] == symbol: count += 1 
            if areas[i[j]] != '<>' and areas[i[j]]!= '><':                 
                free.append(i[j])
        if count==2 and free: result=free[0] 
    return result
             
def robot():
    if areas[4] == 'b2':    
        step = 4
        return step
    for symbol in ('><', '<>'):
        step=checking(symbol)
        if step!=None: 
            return step
    freecells=[i for i in range(len(areas)) if areas[i] != '><' and areas[i] != '<>']
    
    step=int(str(random.choices(freecells))[1])

    return step

def check_win(count, winner):
    win = False
    if count==9 or winner != 0:
        win=True
    return win

def check_winner():
    winner = 0   
    for i in wins_lst:
        if areas[i[0]] == '><' and areas[i[1]] == '><' and areas[i[2]] == '><':
            winner=1 
        if areas[i[0]] == '<>' and areas[i[1]] == '<>' and areas[i[2]] == '<>':
            winner=2
    return winner

printGameArea() 

check = False
while count <9:
    if check == True:
            break
    for player_num in (1,2):
        check=check_win(count, check_winner())
       
        if check == True:
            break

        if player_num==1: smb='><'
        else: smb='<>'
        if ai and player_num==2: 
            areas[robot()] = smb
        else:
            areas[move()] = smb
        printGameArea()
        count +=1
  
print('game over')


print(f'Победил игрок №{check_winner()}')
print('game over')

res=check_winner()
print(check_winner())
if res==0:
    print('Победила дружба! Ничья')
elif res==1:
    print('Победил первый игрок')
elif res==2 and ai:
    print('Победил компьютер.')
else:
    print('Победил второй игрок')