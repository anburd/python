import user_interface
import export_date
import import_date
import search_date


def run():
    while True:
        operation = user_interface.show_menu()
       
        match operation:
            case '1':
                print('\nВнесениe нового контакта')
                import_date.write_contact()
            case '2':
                print('\nПоиск контакта')
                word = input("Введите данные для поиска: ")
                data = export_date.read_contact()
                output = search_date.search_contact(word, data)
                user_interface.print_data(output)
            case '3':
                print('\nВесь справочник:')
                output = export_date.read_contact()
                user_interface.print_data(output)
            case '0':
                exit()

