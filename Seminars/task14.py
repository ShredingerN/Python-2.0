# Пользователь вводит строку из четырёх или более целых чисел, разделённых символом “/”. Сформируйте словарь, где:
# второе и третье число являются ключами
# первое число является значением для первого ключа
# четвертое и все возможные последующие числа хранятся в кортеже как значения второго ключа

# q = '1/2/3/4/5/6/7'
# a, b, c, *d = q.split('/')
# print({b: a, c: tuple(d)})

# Самостоятельно сохраните в переменной строку текста.
# Создайте из строки словарь, где ключ - буква,
# а значение - код буквы. Напишите преобразование в одну строку.

# a = 'qwerty'
# new_gen = {i: ord(i) for i in a}
# print(new_gen)
#
# # Продолжаем развивать задачу 2.
# # Возьмите словарь, который вы получили.
# # Сохраните его итераторатор.
# # Далее выведите первые 5 пар ключ-значение, обращаясь к итератору, а не к словарю.
#
# # в словаре iter идет только по ключам, значения не учитывает
# new_iter = iter(new_gen.items())
#
# for i in range(5):
#     print(next(new_iter))

# Создайте генератор чётных чисел от нуля до 100.
# Из последовательности исключите числа, сумма цифр которых равна 8.
# Решение в одну строку.

# # res = [i for i in range(0, 101) if i % 2 == 0 and (i // 10 + i % 10 != 8)]
# res = [i for i in range(0, 101)
#        if i % 2 == 0
#               and sum(map(int, list(str(i)))) != 8]
# # res = [i for i in range(0, 101,2) if sum(map(int, list(str(i)))) != 8]
# print(res)

# Напишите программу, которая выводит на экран числа от 1 до 100.
# При этом вместо чисел, кратных трем, программа должна выводить слово «Fizz», а вместо чисел, кратных пяти — слово «Buzz».
# Если число кратно и 3, и 5, то программа должна выводить слово «FizzBuzz».
# *Превратите решение в генераторное выражение.

for i in range(1, 100):
    if i % 5 == 0 and i % 3 == 0:
        print('FizzBuzz')
    elif i % 5 == 0:
        print('Buzz')
    elif i % 3 == 0:
        print('Fizz')
    else:
        print(i)
# ветвление if else встают перед for, просто if - после.
res = ['FizzBuzz' if i % 5 == 0 and i % 3 == 0 else
       'Buzz' if i % 5 == 0 else
       'Fizz' if i % 3 == 0 else i
       for i in range(0, 101)]
print(res)

# Создайте функцию-генератор.
# Функция генерирует N простых чисел, начиная с числа 2.
# Для проверки числа на простоту используйте правило:
# “число является простым, если делится нацело только на единицу и на себя”.

import typing


def simpl_n(num: int) -> bool:
    for i in range(2, num):
        if num % i == 0:
            return False
    return True


# n = 100
# for i in range(2, n):
#     if simpl_n(i):
#         print(i)


def gen_simple(n: int) -> typing.Generator:
    for i in range(2, n):
        if simpl_n(i):
            yield i


#
# for i in gen_simple(100):
#     print(i)

result = gen_simple(100)
for i in range(5):
    print(next(result))

# Выведите в консоль таблицу умножения от 2х2 до 9х10 как на школьной тетрадке.

for i in range(2, 10, 4):
    for j in range(2, 11):
        for k in range(i, i + 4):
            print(f'{k:>3} *{j:>3} ={(k * j):>3}', end='\t')
        #   форматирование строк :>3 - добавление пробела
        print()
    print()

# res = [f'{k:>3} *{j:>3} ={(k * j):>3}' for i in range(2, 10, 4) for j in range(2, 11) for k in range(i, i + 4)]
res = [f'{i:>3} *{j:>3} ={(i * j):>3}' for i in range(2, 10) for j in range(2, 10)]
# print('\t'.join(res))



print(*res, sep='\n')

# res = [f'{k:>3} *{j:>3} ={(k * j):>3}' for i in range(2, 10, 4) for j in range(2, 11) for k in range(i, i + 4)]
# говорят, так лучше не исполнять))
res = ['\n'+'\t'.join([f'{k:>3} *{j:>3} ={(k * j):>3}'
                       for k in range(i, i + 4)])
       if i == 6 and j == 2 else '\t'.join([f'{k:>3} *{j:>3} ={(k * j):>3}'
                                            for k in range(i, i + 4)])
       for i in range(2, 10, 4)
       for j in range(2, 11)]

# print('\t'.join(res))


print(*res, sep='\n')
