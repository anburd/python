# Реализуйте RLE алгоритм: реализуйте модуль сжатия и восстановления данных.
# Входные и выходные данные хранятся в отдельных текстовых файлах.

# Считываем файл
with open('task3_RLE_incoming.txt', 'r') as data:
    inc_string = data.read()
print('Входящая строка:')
print(inc_string)


def encoding(incom_str):
    """
    Функция RLE кодирования входящей строки
    """
    encod_str = ""
    prev_char = incom_str[0]
    count = 0
    for i in incom_str:
        if i == prev_char:
            count += 1
        else:
            encod_str += str(count) + prev_char
            prev_char = i
            count = 1
    encod_str += str(count) + prev_char
    return encod_str


def decoding(text):
    """
    Функция RLE декодирования входящей строки
    """
    decod_str = ''
    digit = ''
    for i in range(len(text)):
        if str(text[i]).isdigit():
            digit = digit + str(text[i])
        else:
            if digit != '':
                for j in range(int(digit)):
                    decod_str += text[i]
                digit = ''
    return decod_str


# кодируем строку
coded_string = encoding(inc_string)

# и записываем в файл
with open('task3_RLE_coding.txt', 'w') as out:
    out.write(coded_string)

# для проверки - смотрим результат
print('Закодированная строка:')
print(coded_string)


# разкодируем строку
out_string = decoding(coded_string)

# и тоже записываем в файл
with open('task3_RLE_out.txt', 'w') as out:
    out.write(out_string)
    
# для проверки - смотрим результат
print('Разкодированная строка:')
print(out_string)
