
def read_contact():
    data = []
    with open('phones.csv', 'r', encoding='utf-8') as file:
        for line in file:
            data.append(line.strip().split(';'))

        return data
