
def read_data():
    with open('phones.csv', 'r', encoding = 'utf-8') as file:
        for line in file:
            print(line)
read_data()