# 34. *Даны два файла, в каждом из которых находится запись многочлена.
# Задача - сформировать файл, содержащий сумму многочленов.
# 2x² + 4x + 5 = 0 и x² + 5x + 3 = 0 => 3x² + 9x + 8 = 0

# сделал только если оба многочлена одной длины как в примере


# считываем многочлен из файла и выделем его коэффициенты с список,
# при этом восстанавливаем '1' так как она не пишется ( x => 1x)
with open('task34_1.txt', 'r') as data:
    lst1 = data.read()
    print(f'первый многочлен: {lst1}')
    lst1 = lst1.replace('=', '').replace('0', '').replace('^2', '').replace('+', '').replace('x', '').split()

for i in range(len(lst1)):
    if lst1[i] == 'x':
        lst1[i] = "1"
    lst1[i] = lst1[i].replace('x', '')

# повторяем со 2 файлом
with open('task34_2.txt', 'r') as data:
    lst2 = data.read()
    print(f'второй многочлен: {lst2}')
    lst2 = lst2.replace('=', '').replace('0', '').replace('^2', '').replace('+', '').split()

for i in range(len(lst2)):
    if lst2[i] == 'x':
        lst2[i] = "1"
    lst2[i] = lst2[i].replace('x', '')

# перемножаем коэффициенты
lst_new = [int(lst1[i]) + int(lst2[i]) for i in range(len(lst1))]

# составляем итоговый многочлен
polynomial_sum = str(lst_new[0])+'x^2 + ' + str(lst_new[1]) + 'x + ' + str(lst_new[2]) + ' = 0'

print(f'сумма многочленов: {polynomial_sum}')

# записываем в файл
with open('task34_res.txt', 'w') as out:
    out.write(polynomial_sum)
