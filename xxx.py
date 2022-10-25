import os
import random
areas = ['><', '><', '<>', 'b1', '<>', 'b3', '><', 'c2', 'c3']

player_num=1

def printGameArea():

    # os.system('cls' if os.name == 'nt' else 'clear')
    for i in range(0, 9, 3):
        print('----------------')
        print('|', areas[i], '|', areas[i+1], '|', areas[i+2], '|')
    print('----------------')
printGameArea()

smb = ('><')
wins_lst = [[0, 1, 2], [3, 4, 5], [6, 7, 8], [0, 3, 6], [1, 4, 7], 
[2, 5, 8], [0, 4, 8], [2, 4, 6]]   
    



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
    for symbol in ('><', '<>'):
        step=checking(symbol)
        if step!=None: 
            return step
    freecells=[i for i in range(len(areas)) if areas[i] != '><' and areas[i] != '<>']
    step=random.choices(freecells)
    return step


freecells=[i for i in range(len(areas)) if areas[i] != '><' and areas[i] != '<>']
#st=str(random.choices(freecells))

step=int(str(random.choices(freecells))[1])

print(type(step), step)






