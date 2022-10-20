# 33. Задана натуральная степень k. Сформировать случайным образом список коэффициентов 
# (значения от 0 до 100) многочлена и записать в файл многочлен степени k.
# Пример:
# k=2 => 2x² + 4x + 5 = 0 или x² + 5 = 0 или 10x² = 0
from random import randint as rnd
k=2

lst_k = [rnd(0, 1) for i in range(k+1)]

    

lst= lst_k[::-1]
wr = ''
if len(lst) < 1:
    wr = 'x = 0'
else:
    for i in range(len(lst)):
        if i != len(lst) - 1 and lst[i] != 0 and i != len(lst) - 2:
            wr += f'{lst[i]}x^{len(lst)-i-1}'
            if lst[i+1] != 0 or lst[i+2] != 0:
                wr += ' + '
        elif i == len(lst) - 2 and lst[i] != 0:
            wr += f'{lst[i]}x'
            if lst[i+1] != 0 or lst[i+2] != 0:
                wr += ' + '
        elif i == len(lst) - 1 and lst[i] != 0:
            wr += f'{lst[i]} = 0'
        elif i == len(lst) - 1 and lst[i] == 0:
            wr += ' = 0'

print(wr)