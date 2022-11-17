# модуль поиска контакта


def search_contact(word, data):
    out = list(filter(lambda x: word in x, data))
    if len(out) == 0:
        out = ['нет данных']
    return out
