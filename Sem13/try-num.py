# Создайте функцию, которая запрашивает числовые данные от пользователя до тех пор,
# пока он не введёт целое или вещественное число. Обрабатывайте не числовые данные как исключения.

def ask_user():
    while True:
        try:
            num = int(input('введите число: '))
            print('ok')
            return num
        except ValueError:
        # except Exception:
            print('это не число, введитe еще раз')


a = ask_user()
print(a)
