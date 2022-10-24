import os
import random
areas = ['a1', 'a2', 'a3', 'b1', 'b2', 'b3', 'c1', 'c2', 'c3']
count = 0
player_num=1



smb = ('><')
wins_lst = [[0, 1, 2], [3, 4, 5], [6, 7, 8], [0, 3, 6], [1, 4, 7], 
[2, 5, 8], [0, 4, 8], [2, 4, 6]]


def printGameArea():

    # os.system('cls' if os.name == 'nt' else 'clear')
    for i in range(0, 9, 3):
        print('----------------')
        print('|', areas[i], '|', areas[i+1], '|', areas[i+2], '|')
    print('----------------')

def move():
    step = ''
    print(f'Игрок {player_num}')
    while step not in areas:
        step = input('ваш ход: ')
    areas[areas.index(step)] = smb

def robot():
    step_index = 10
    if areas[4] == 'b2':    
        step_index = 4
    
    no_x=0
    no_o=0
    
    for i in wins_lst:
        x = 0
        for j in range(3):
            if  areas[i[j]] == '><':
                x += 1   
            if x==2: break 

        for j in range(3):
            if areas[i[j]] != '><' and areas[i[j]] != '<>':
                no_x=i[j]
        if x==2: break    

    if step_index == 10: step_index = no_x      

    for i in wins_lst:
        o = 0
        for j in range(3):  
            if areas[i[j]] == '<>':
                o += 1   
            if o==2: break 
        for j in range(3):
            if areas[i[j]] != '><' and areas[i[j]] != '<>':
                no_o=i[j]
        if o==2: break    

    if step_index == 10: step_index = no_o 


    # freecells=[]
    # for i in range(len(areas)):
    #     if areas[i] != '><' and areas[i] != '<>':
    #         freecells.append(i)
    #         print(freecells)
    # if step_index == 10: step_index = random.choices(freecells)
    # print(random.choices(freecells))
    print(step_index)
    print(areas[step_index] )
    areas[step_index] = smb

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
    move()
    printGameArea()
    count +=1

   
    check=check_win(count, check_winner())
    if check == True:
        break
    player_num = 2
    smb = ('<>') 
    player2()
    count +=1
    printGameArea()

  

print('game over')


print(f'Победил игрок №{check_winner()}')

