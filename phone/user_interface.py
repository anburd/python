def choise_operation():
    print('Телефонный справочник.\n')
    operation = int(input('Выберите операцию: \n \
        1 - Внести новый контакт. \n \
        2 - Найти контакт. \n \
        3 - Вывести весь список контактов.\n \
        Ваш выбор: '))
    return operation


def print_data(data):
    print(*(' '.join(x) for x in data), sep='\n')
