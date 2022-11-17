def write_contact():
    entry = []
    surname = input('Введите фамилию: ')
    entry.append(surname)
    name = input('Введите имя: ')
    entry.append(name)
    phone = input('Введите телефон: ')
    entry.append(phone)
    description = input('Введите описание контакта: ')
    entry.append(description)

    with open('phones.csv', 'a', encoding='utf-8') as file:
        file.write(
            f'{entry[0]};{entry[1]};{entry[2]};{entry[3]}\n')
