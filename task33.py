# 33. Задана натуральная степень k. Сформировать случайным образом список коэффициентов 
# (значения от 0 до 100) многочлена и записать в файл многочлен степени k.
# Пример:
# k=2 => 2x² + 4x + 5 = 0 или x² + 5 = 0 или 10x² = 0
from random import randint 

k=2



lst_k = [randint(0, 100) for i in range(k+1)]

print(lst_k)
   
polynomial = str(lst_k[0])+'x^2 + ' + str(lst_k[1]) + 'x + ' + str(lst_k[2]) + ' = 0'

print(polynomial)

lst_step=[]

for i in range(0, k+1):
    lst_step.append('x^' + str(k-i))

print(lst_step)

poly=[]
for i in range(0, k+1):
    print(lst_k[i])
    print(lst_step[i])

    poly.append(str(lst_k[i]) + str(lst_step[i]))

poly_str=' + '.join(poly)

print(poly_str)
poly_str=poly_str.replace('x^1', 'x').replace('x^0', '')+' = 0'

print(poly_str)
