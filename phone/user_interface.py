def show_menu():
    print('\nТелефонный справочник.\n'
        'Выберите операцию: \n \
        1 - Внести новый контакт. \n \
        2 - Найти контакт. \n \
        3 - Вывести весь список контактов. \n \
        0 - Выход' )
    operation = input('Ваш выбор:')
    return  operation


def print_data(data):
    print(*(' '.join(x) for x in data), sep='\n')
