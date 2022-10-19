
# 18. *Реализуйте алгоритм перемешивания списка.

# так как нужно придумать алгоритм без использования random и shuffle 
# создаю свою функцию получения случайного числа на основе системного времени

def get_rand(х):
    import datetime
    return datetime.datetime.now().microsecond % х


initial_list = [1, 2, 3, 4, 5, 6, 7, 8, 9]


print(f'Первоначальный список: {initial_list}')


def myShuffl(list):
    n = get_rand(len(list))

    for a in range(n+1):  # глубина смешивания, т.е. сколько раз пройтись, задается случайно

        for i in range(len(list)): # получаем случайный индекс в списке

            index_rnd = get_rand(len(list))

            if i != index_rnd:  # проверка, чтобы значение позиции не менялось само с собой
           
                tmp = list[i]  # меняем значение позиции с значением случайной позиции
                list[i] = list[index_rnd]
                list[index_rnd] = tmp

    return list


print(f'Перемешанный  список:  {myShuffl(initial_list)}')
