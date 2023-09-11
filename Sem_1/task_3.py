# Нарисовать в консоли ёлку спросив у пользователя количество рядов.
# Пример результата:
# Сколько рядов у ёлки? 5
#     *
#    ***
#   *****
#  *******
# *********

rows = int(input("Enter number of rows: "))
STAR = '*'
SPACE = ' '
count_spaces = rows - 1
count_stars = 1
COEFF = 2
for row in range(rows):
    print(SPACE * (count_spaces - row) + STAR * (count_stars + row * COEFF))
