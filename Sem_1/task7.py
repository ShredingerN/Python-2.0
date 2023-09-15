# Напишите программу, которая вычисляет площадь круга и длину окружности по введённому диаметру. Диаметр не превышает
# 1000 у.е. Точность вычислений должна составлять не менее 42 знаков после запятой.

import decimal
import math

decimal.getcontext().prec = 42
d = decimal.Decimal(input('введите число: '))
pi = decimal.Decimal(math.pi)

s = pi * pow(d, 2) / 4
l = pi * d

print(s, l)
