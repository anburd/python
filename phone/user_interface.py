def show_menu():
    print('\nТелефонный справочник.\n'
        'Выберите операцию: \n \
        1 - Внести новый контакт. \n \
        2 - Найти контакт. \n \
        3 - Вывести весь список контактов. \n \
        0 - Выход' )
    operation = input('Ваш выбор:')
    return  operation


def choice_format():
    print('\nВывести справочник: \n \
        1 - на экран. \n \
        2 - в формат HTML. \n \
        3 - в формат . ' )
    format = input('Ваш выбор:')
    return  format