import user_interface
import export_date
import import_date
import search_date


def run():
    operation = user_interface.choise_operation()

    if operation == 1:
        print('Внесениe нового контакта')
        import_date.write_contact()

    if operation == 2:
        print('Поиск контакта')
        word = input("Введите данные для поиска: ")
        data = export_date.read_contact()
        output = search_date.search_contact(word, data)
        user_interface.print_data(output)

    if operation == 3:
        print('Весь справочник:')
        output = export_date.read_contact()
        user_interface.print_data(output)

