# Задача №32: Задайте последовательность чисел.
# Напишите программу, которая выведет список неповторяющихся элементов исходной последовательности.


# lst = list(map(int, input("Введите числа через пробел:\n").split()))

lst = [14, 1, 3, 5, 4, 9, 14, 5, 1]
print(f"Исходный список: {lst}")


# Вариант 1: [14, 1, 3, 5, 4, 9, 14, 5, 1] => [1, 3, 4, 5, 9, 14]

new_lst = list(set(lst))
# [new_lst.append(i) for i in lst if i not in new_lst]

print('вариант 1:')
print(f"Список из неповторяющихся элементов: {new_lst}")

# Вариант 2: [14, 1, 3, 5, 4, 9, 14, 5, 1] => [3, 4, 9]

new_lst_alone = []
for i in range(0, len(lst)):
    flag = True
    for j in range(0, len(lst)):
        if i != j:
            if lst[i] == lst[j]:
                flag = False
    if flag: new_lst_alone.append(lst[i])

print('вариант 2:')
print(f"Список из неповторяющихся элементов: {new_lst_alone}")
