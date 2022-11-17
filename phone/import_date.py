def write_contact():
    element = []
    surname = input('Введите фамилию: ')
    element.append(surname)
    name = input('Введите имя: ')
    element.append(name)
    phone = input('Введите телефон: ')
    element.append(phone)
    description = input('Введите описание контакта: ')
    element.append(description)

    with open('phones.csv', 'a', encoding='utf-8') as file:
        file.write(
            f'{element[0]};{element[1]};{element[2]};{element[3]}\n')
