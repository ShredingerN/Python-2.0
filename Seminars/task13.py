# Напишите функцию, которая принимает строку текста. Вывести функцией каждое слово с новой строки.
# Строки нумеруются начиная с единицы
# Слова выводятся отсортированными согласно кодировки Unicode
# Текст выравнивается по правому краю так, чтобы у самого длинного слова был один пробел между ним и номером строки


# def str_text(n:str)->str:
#     '''Работа со строкой.'''
#     b = ''
#     a = sorted(n.split())
#     max_len = 0
#     # max_len = len(max(a, key=len))
#     for el in a:
#         if len(el) > max_len:
#             max_len = len(el)
#     for n, el in enumerate(a, start=1):
#         b += f'{n} {el:>{max_len}}\n'
#     return b
#
#
# n = input()
# print(str_text(n))

# Напишите функцию, которая принимает строку текста.
# Сформируйте список с уникальными кодами Unicode каждого символа введённой строки отсортированный по убыванию.
#
# def text_ord(n: str) -> list[int]:
#     d = set()
#     for el in n:
#         d.add(ord(el))
#     return sorted(list(d), reverse=True)
#     # return sorted(list(set(map(ord, list(n)))), reverse=True)
#
#
# n = input()
# print(text_ord(n))
# # print(text_ord(input()))

# ✔ Функция получает на вход строку из двух чисел через пробел.
# ✔ Сформируйте словарь, где ключом будет
# символ из Unicode, а значением — целое число.
# ✔ Диапазон пар ключ-значение от наименьшего из введённых
# пользователем чисел до наибольшего включительно.

# def str_int(a: str) -> dict[str, int]:
#     f = {}
#     start, stop = map(int, a.split())
#     for i in range(start, stop):
#         f[chr(i)] = i
#     return f
#
#
# b = input()
# print(str_int(b))


# Функция получает на вход список чисел. Отсортируйте его элементы in place без использования встроенных в язык сортировок.
# Как вариант напишите сортировку пузырьком. Её описание есть в википедии.

# def my_func(abc: list[int]):
#     for i in range(len(abc)):
#         for j in range(i, len(abc)):
#             if abc[i] > abc[j]:
#                 abc[i], abc[j] = abc[j], abc[i]
#
#
# my_l = [1, 4, 7, 8, 0, 2, 3, 4]
# my_func(my_l)
# print(my_l)

# Функция принимает на вход три списка одинаковой длины: имена str, ставка int, премия str с указанием процентов вида “10.25%”.
# Вернуть словарь с именем в качестве ключа и суммой премии в качестве значения.
# Сумма рассчитывается как ставка умноженная на процент премии

# def my_f(names: list[str], salaries: list[int], bonuses: list[str]) -> dict[str, float | int]:
#     result = {}
#     for name, salary, bonus in zip(names, salaries, bonuses):
#         result[name] = salary * (float(bonus[:-1]) / 100)
#     return result
#
#
# n = ["Иван", "Николай", "Пётр", "Харитон"]
# s = [125_000, 96_000, 109_000, 100_000]
# a = ['10%', '25.5%', '13.3%', '42.73%']
# print(my_f(n, s, a))


# Функция получает на вход список чисел и два индекса. Вернуть сумму чисел между между переданными индексами.
# Если индекс выходит за пределы списка, сумма считается до конца и/или начала списка. Если нижняя граница меньше нуля,
# суммируем от начала. Если верхняя граница больше длины списка, до конца.

# def nums(numbers: list[int], start: int, stop: int) -> int:
#     if start > stop:
#         start, stop = stop, start
#     if start < 0 or start > len(numbers):
#         start = 0
#     if stop > len(numbers) or stop < 0:
#         stop = len(numbers)
#     return sum(numbers[start:stop])
#
#
# numbers = [4, 6, 1, 2, 5, 0, 3]
# print(nums(numbers, 10, 20))

# Функция получает на вход словарь с названием компании в качестве ключа и списком с доходами и расходами (3-10 чисел)
# в качестве значения.
# Вычислите итоговую прибыль или убыток каждой компании.
# Если все компании прибыльные, верните истину, а если хотя бы одна убыточная - ложь.

# def company(llc: dict[str, int | float]) -> bool:
#     for key, value in llc.items():
#         if sum(value) < 0:
#             return False
#     return True

# def is_profit(companys: dict[str, int | float]) -> bool:
#     return all(map(lambda x: sum(x) > 0, companys.values()))
# data = {
#     "Рога": [42, -73, 12, 85, -15, 2],
#     "Копыта": [45, 25, -100, 22, 1],
#     "Хвосты": [-500, 123, 52, 45, 93],
# }
# # print(company(data))
# print(is_profit(data))

# Создайте несколько переменных заканчивающихся и не оканчивающихся на “s”.
# Напишите функцию, которая при запуске заменяет содержимое переменных оканчивающихся на s
# (кроме переменной из одной буквы s) на None. Значения не удаляются, а помещаются в одноимённые переменные без s на конце.

def change():
    a = globals()
    for key, value in a.items():
        if key[-1] == 's':
            a[key[:-1]] = value
            a[key] = None


cat = '1'
cats = '2'
dog = '3'
dogs = '4'
change()
print(globals())
