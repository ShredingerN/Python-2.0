"""
Напишите программу, которая запрашивает год и проверяет его на високосность.
Распишите все возможные проверки в цепочке elif
Откажитесь от магических чисел
Обязательно учтите год ввода Григорианского календаря
В коде должны быть один input и один print
"""
MAIN_DIVIDER = 4
EXEPTION_DIVIDER = 100
ADD_DIVIDER = 400
year = int(input("Введите год: "))
if (year % MAIN_DIVIDER == 0
        and year % EXEPTION_DIVIDER != 0) \
        or year % ADD_DIVIDER == 0:
    print("Год високосный")
else:
    print("Год обычный")
