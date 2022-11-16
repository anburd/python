# модуль поиска контакта

from export_data import read_data

word = input("Введите данные для поиска: ")
data = read_data()

def search_data(word, data):
    for item in data:
        if word in item:
            return item
    else:
        return None



search_data(word, data)