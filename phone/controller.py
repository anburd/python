import record
import user_interface
import export_data
import import_data

def run():
    operation = user_interface.choise_operatoin()
    
    if operation == 1:
        print('Выбрана операция внесения нового контакта.')
        import_data.input_format(record.record())


    if operation == 2:
        print('Выбрана операция вывода справочника.')
        
        export_data.read_data()

        