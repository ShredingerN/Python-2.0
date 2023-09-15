# Напишите программу банкомат.
# Начальная сумма равна нулю
# Допустимые действия: пополнить, снять, выйти
# Сумма пополнения и снятия кратны 50 у.е.
# Процент за снятие - 1.5% от суммы снятия, но не менее 30 и не более 600 у.е.
# После каждой третей операции пополнения или снятия начисляются проценты - 3%
# Нельзя снять больше, чем на счёте
# При превышении суммы в 5 млн, вычитать налог на богатство 10% перед каждой операцией, даже ошибочной
# Любое действие выводит сумму денег

s = 10000
count = 1
PERCENT = 0.015
MIN_COM = 30
MAX_COM = 600
MAX_LIMIT = 5_000_000
OPERATIONS = 3
BONUS = 1.03
DIVIDER = 50
TAX = 0.9

while True:
    action = input('Введите операцию 1 - пополнение,2 - снятие, 3 - выйти: ')
    if s >= MAX_LIMIT:
        s *= TAX
    if count % OPERATIONS == 0 and count != 0:
        s *= BONUS
        count = 1
    if action == '1':
        withdrow = int(input('введите сумму: '))
        if withdrow % DIVIDER == 0:
            count += 1
            s += withdrow
    elif action == '2':
        withdrow = int(input('введите сумму: '))
        if withdrow % DIVIDER == 0:
            comission = withdrow * PERCENT
            if comission < MIN_COM:
                comission = MIN_COM
            elif comission > MAX_COM:
                comission = MAX_COM
            if (comission + withdrow) < s:
                s -= (withdrow + comission)
                count += 1
    else:
        break
    print(s)
