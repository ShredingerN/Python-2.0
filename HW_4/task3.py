# Возьмите задачу о банкомате из семинара 2. Разбейте её на отдельные операции — функции.
# Дополнительно сохраняйте все операции поступления и снятия средств в список.


def tax():
    global balance
    MAX_LIMIT = 5_000_000
    TAX = 0.9
    if balance >= MAX_LIMIT:
        balance *= TAX
    return balance


def bonus():
    global balance, count, DIVIDER, amount
    BONUS = 1.03
    OPERATIONS = 3
    if count % OPERATIONS == 0 and count != 0:
        balance *= BONUS
        count = 1
    return balance


def deposit():
    global balance, count, log1
    amount = int(input('Введите сумму: '))
    DIVIDER = 50
    if amount % DIVIDER == 0:
        balance += amount
        count += 1
        log1.append(amount)
        return balance


def withdraw():
    global balance, count, log2
    amount = int(input('Введите сумму: '))
    PERCENT = 0.015
    MIN_COM = 30
    MAX_COM = 600
    DIVIDER = 50
    if amount % DIVIDER == 0:
        comission = amount * PERCENT
        if comission < MIN_COM:
            comission = MIN_COM
        elif comission > MAX_COM:
            comission = MAX_COM
        if (comission + amount) <= balance:
            balance -= (amount + comission)
            count += 1
            log2.append(amount)
    return balance


balance = 0
count = 1
log1 = []
log2 = []

while True:
    action = input('Введите операцию 1 - пополнение, 2 - снятие, 3 - выйти: ')
    result = tax()
    result = bonus()
    if action == '1':
        result = deposit()
    elif action == '2':
        result = withdraw()
    else:
        break
    print(f'Баланс счета: {result}')
    print(f'История пополнения: {log1}\nИстория снятия:{log2}')
