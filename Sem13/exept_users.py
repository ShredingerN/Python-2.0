# Вспоминаем задачу из семинара 8 про сериализацию данных, где в бесконечном цикле запрашивали имя, личный идентификатор
# и уровень доступа (от 1 до 7) сохраняя информацию в JSON файл. Напишите класс пользователя, который хранит эти данные
# в свойствах экземпляра. Отдельно напишите функцию, которая считывает информацию из JSON файла и
# формирует множество пользователей.

# Доработаем задачи 3 и 4. Создайте класс проекта, который имеет следующие методы:
# загрузка данных (функция из задания 4)
# вход в систему - требует указать имя и id пользователя.
# Для проверки наличия пользователя в множестве используйте магический метод проверки на равенство пользователей.
# Если такого пользователя нет, вызывайте исключение доступа. А если пользователь есть,
# получите его уровень из множества пользователей.
# добавление пользователя. Если уровень пользователя меньше, чем ваш уровень, вызывайте исключение уровня доступа.


import json
from my_except import ErrorAccess, ErrorLevel


class Project:
    def __init__(self, file_name):
        self.users = read(file_name)
        self.admin = User(None, None, None)

    def enter(self, name, id):
        temp_user = User(name, id, None)
        if temp_user not in self.users:
            raise ErrorAccess(id, name)
        for user in self.users:
            if user == temp_user:
                self.admin = user

    def add_user(self, new_name, new_id, new_lvl):
        if int(new_lvl) < int(self.admin.lvl):
            raise ErrorLevel (self.admin.lvl, new_lvl)
        self.user.add(User(new_name, new_id, new_lvl))


class User:
    def __init__(self, name, id, lvl):
        self.name = name
        self.id = id
        self.lvl = lvl

    def __repr__(self):
        return f'User {self.name}, {self.id}, {self.lvl}'

    def __eq__(self, __value: object) -> bool:
        return self.id == __value.id and self.name == __value.name

    def __hash__(self) -> int:
        return hash(self.id)


def read(file_name):
    new_set = set()
    with open(file_name, 'r') as f:
        data = json.load(f)
    for lvl, user in data.items():
        for id, name in user.items():
            new_set.add(User(name, id, lvl))
    return new_set


def data(name: str, id: str, level: str, file_name):
    try:
        with open(file_name, 'r', encoding='utf-8') as f:
            users = json.load(f)
    except FileNotFoundError:
        users = {'1': {}, '2': {}, '3': {}, '4': {}, '5': {}, '6': {}, '7': {}}
    users[level][id] = name
    with open(file_name, 'w', encoding='utf-8') as f:
        json.dump(users, f, ensure_ascii=False)


def request(file_name):
    while True:
        name = input('Введите имя: ')
        id = input('Введите id: ')
        level = input('Введите уровень: ')
        data(name, id, level, file_name)


# print(read('users1.json'))
new_p = Project('users1.json')
new_p.enter("fgh", "4")
new_p.add_user("new_user", "11", "1")
print(new_p.users)
