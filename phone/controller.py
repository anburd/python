import user_interface
import export_date
import import_date
import search_date
import html_creater
def print_data(data):
    print(*(' '.join(x) for x in data), sep='\n')



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
                print_data(output)
            case '3':
                format = user_interface.choice_format()
                output = export_date.read_contact()
                if format == '1':
                    print_data(output)
                elif format == '2':
                    html_creater.create(output)
                # elif format == '3':                  

            case '0':
                exit()

