# import sys
#
# t = "123445567"
# print(str.isdecimal(t))
# # print(bin(t))
# # print(oct(t))
# # print(hex(t))
#
# print(str.isascii(t))
# # print(str.isalnum(t))
#
# data = [25, -42, 146, 73, -100, 12]
# print(list(map(str, data)))
# # переделывает применяем - ко всем числам в списке и возвращаем макс
# print(max(data, key=lambda x: -x))
# # х - ключ-значение, убираем даденр методы
# print(*filter(lambda x: not x[0].startswith('__'), globals().items()))

import json


#
# with open('user.json', 'r', encoding='utf-8') as f:
#     json_file = json.load(f)
#
# print(f'{type(json_file) = }\n{json_file = }')
# print(f'{json_file["name"] = }')
# print(f'{json_file["address"]["geo"] = }')
# print(f'{json_file["email"] = }')

# a = 'Hello world!'
# b = {key: value for key, value in enumerate(a)}
# c = json.dumps(b, indent=3, separators=('; ', '= '))
# print(c)

#
# class Person:
#     max_up = 3
#
#     def __init__(self, name, race='unknown'):
#         self.name = name
#         self.race = race
#         self.level = 1
#         self.health = 100
#
#     def level_up(self):
#         self.level += 1
#
#
# p1 = Person('Сильвана', 'Эльф')
# p2 = Person('Иван', 'Человек')
# p3 = Person('Грогу')
# print(f'{p1.level = }, {p2.level = }, {p3.level = }')
# p3.level_up()
# p1.level_up()
# p3.level_up()
# print(f'{p1.level = }, {p2.level = }, {p3.level = }')
#
#
# class User:
#     count = []
#
#     def __init__(self, name, phone):
#         self.name = name
#         self.phone = phone
#
#
# u1 = User('One', '123-45-67')
# u2 = User('NoOne', '76-54-321')
# u1.count.append(42)
# u1.count.append(73)
# u2.counter = 256
# u2.count.append(u2.counter)
# u2.count.append(u1.count[-1])
# print(f'{u1.name = }, {u1.phone = }, {u1.count = }')
# print(f'{u2.name = }, {u2.phone = }, {u2.count = }')
#
#
# class A:
#     name = 'A'
#     def call(self):
#         print(f'I am {self.name}')
# class B:
#     name = 'B'
#     def call(self):
#         print(f'I am {self.name}')
# class C:
#     name = 'C'
#     def call(self):
#         print(f'I am {self.name}')
# class D(C, A):
#     pass
# class E(D, B):
#     pass
# e = E()
# e.call()

# class User:
#     def __init__(self, name: str, equipment: list = None):
#         self.name = name
#         self.equipment = equipment if equipment is not None else []
#         self.life = 3
#         # принтим только в учебных целях, а не для реальных задач
#         print(f'Создал {self} со свойствами:\n'
#               f'{self.name = },\t{self.equipment = },\t{self.life=}')
#
#
# print('Создаём первый раз')
# u_1 = User('Спенглер')
# print('Создаём второй раз')
# u_2 = User('Венкман', ['протонный ускоритель', 'ловушка'])
# print('Создаём третий раз')
# u_3 = User(equipment=['ловушка', 'прибор ночного видения'],
#            name='Стэнц')


class Singleton:
    _instance = None

    def __new__(cls, *args, **kwargs):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
        return cls._instance

    def __init__(self, name: str):
        self.name = name


a = Singleton('Первый')
print(f'{a.name = }')
b = Singleton('Второй')
print(f'{a is b = }')
print(f'{a.name = }\n{b.name = }')


class User:
    def __init__(self, name: str):
        """Added the name parameter."""
        self.name = name

    def simple_method(self):
        """Example of a simple method."""
        self.name.capitalize()

    def __str__(self):
        return f'Экземпляр класса User с именем "{self.name}"'


user = User('Спенглер')
print(user)


class User:
    def __init__(self, name: str):
        self.name = name

    def simple_method(self):
        self.name.capitalize()

    def __repr__(self):
        return f'User({self.name})'


user = User('Спенглер')
print(user)
