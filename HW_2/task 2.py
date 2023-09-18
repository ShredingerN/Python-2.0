# Напишите программу, которая принимает две строки вида “a/b” - дробь с числителем и знаменателем.
# Программа должна возвращать сумму и произведение* дробей. Для проверки своего кода используйте модуль fractions.

import math
from fractions import Fraction as F

try:
    fraction_1 = input('введите дробь 1 в виде x/y: ')
    fraction_2 = input('введите дробь 2 в виде x/y: ')
    print()
    # преобразуем строку в целочисленный список
    fract1 = [int(x) for x in fraction_1.split("/")]
    fract2 = [int(x) for x in fraction_2.split("/")]

    if fract1[1] <= 0 or fract2[1] <= 0:
        print('Знаменатель не может быть отрицательным или равен 0!')
    else:
        def sum_fractions(f1, f2):
            numerator = f1[0] * f2[1] + f2[0] * f1[1]
            denominator = f1[1] * f2[1]
            res = list(reduce_fraction(numerator, denominator))
            if abs(res[0]) > res[1] != 1:
                # не исключаю ввод отрицательного числителя, поэтому добавила модуль.
                # округляю через round, т.к. целочисленное деление при отрицательном числителе
                # округляет не в ту сторону.
                int_part = round((res[0] / res[1]))
                final_res = (f'{res[0]}/{res[1]} - неправильная дробь, выделим целую часть: '
                             f'{int_part} и {abs(res[0]) - abs(int_part) * res[1]}/{res[1]}')
            elif abs(res[0]) == res[1] or res[1] == 1:
                final_res = (f'{res[0]}/{res[1]} --> {res[0]}')
            else:
                final_res = f'{res[0]}/{res[1]}'
            return final_res


        def multiply_fractions(f1, f2):
            numerator = f1[0] * f2[0]
            denominator = f1[1] * f2[1]
            res = list(reduce_fraction(numerator, denominator))
            if abs(res[0]) > res[1] != 1:
                int_part = round((res[0] / res[1]))
                final_res = (f'{res[0]}/{res[1]} - неправильная дробь, выделим целую часть: '
                             f'{int_part} и {abs(res[0]) - abs(int_part) * res[1]}/{res[1]}')
            elif abs(res[0]) == res[1] or res[1] == 1:
                final_res = (f'{res[0]}/{res[1]} --> {res[0]}')
            else:
                final_res = f'{res[0]}/{res[1]}'
            return final_res


        # сокращаем дробь через НОД
        def reduce_fraction(a, b):
            return a // math.gcd(a, b), b // math.gcd(a, b)


        print(f'сумма дробей: {sum_fractions(fract1, fract2)}')
        print(f'сумма дробей через модуль Fractions: {F(fraction_1) + F(fraction_2)}')
        print()
        print(f'произведение дробей: {multiply_fractions(fract1, fract2)}')
        print(f'произведение дробей через модуль Fractions: {F(fraction_1) * F(fraction_2)}')

except (NameError, IndexError, ValueError):
    print('Ошибка! Введите дробь в корректной форме - x/y.')
