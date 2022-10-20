# 30. Есть два файла: в одном хранятся ФИО пользователей сайта, а в другом — данные об их хобби.
#  Известно, что при хранении данных используется принцип: одна строка — один пользователь.
#  Написать код, загружающий данные из обоих файлов и формирующий из них словарь:
#  ключи — ФИО, значения — данные о хобби.
users_hobby_dic = {} 

with open('users.txt', 'r', encoding='utf8') as user_name, open('hobby.txt', "r", encoding="utf-8") as hobby_name:

    users_hobby_dic = dict(zip(user_name.read().split('\n'), hobby_name.read().split('\n')))

print(users_hobby_dic)



with open('users_hobby.txt', 'w', encoding='utf8') as out:
        for key, val in users_hobby_dic.items():
            out.write('{}: {}\n'.format(key, val))