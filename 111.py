import os
import random
areas = ['a1', 'a2', 'a3', 'b1', 'b2', 'b3', 'c1', 'c2', 'c3']
count = 0
player_num=1



smb = ('><')
wins_lst = [[0, 1, 2], [3, 4, 5], [6, 7, 8], [0, 3, 6], [1, 4, 7], 
[2, 5, 8], [0, 4, 8], [2, 4, 6]]


def printGameArea():

    os.system('cls' if os.name == 'nt' else 'clear')
    for i in range(0, 9, 3):
        print('----------------')
        print('|', areas[i], '|', areas[i+1], '|', areas[i+2], '|')
    print('----------------')

def move():
    step = ''
    print(f'Игрок {player_num}')
    while step not in areas:
        step = input('ваш ход: ')
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

print(robot())

# player2=move
player2=robot

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

while count <9:
    check=check_win(count, check_winner())
    if check == True:
        break
    player_num = 1
    smb = ('><')
    areas[areas.index(move())] = smb
    printGameArea()
    count +=1

   
    check=check_win(count, check_winner())
    if check == True:
        break
    player_num = 2
    smb = ('<>') 
    areas[player2()] = smb    
    printGameArea()
    count +=1

  

print('game over')


print(f'Победил игрок №{check_winner()}')