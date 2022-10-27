areas = ['a1', 'a2', 'a3', 'b1', 'b2', 'b3', 'c1', 'c2', 'c3']
    

print
def draw_board():
    cor=('a','b','c') 
    not_areas = ['a1', 'a2', 'a3', 'b1', 'b2', 'b3', 'c1', 'c2', 'c3']
    print('   ', '1', ' ', '2', ' ', '3', '   ')
    print(' ','-' * 13)
    for i in range(3):
        if areas[0+i*3] not in not_areas:
            a1=areas[0+i*3]
        else: a1=' '
        if areas[1+i*3] not in not_areas:
            a2=areas[1+i*3]
        else: a2=' '
        if areas[2+i*3] not in not_areas:
            a3=areas[2+i*3]
        else: a3=' '
        print(cor[i], "|", a1, "|", a2, "|", a3, "|")
        print(' ','-' * 13)

draw_board()