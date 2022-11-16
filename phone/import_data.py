import datetime
import record

def input_format(entry):

    with open('phones.csv', 'a', encoding = 'utf-8') as file:
        file.write(f'{entry[0]};{entry[1]};{entry[2]};{entry[3]}\n\n')
