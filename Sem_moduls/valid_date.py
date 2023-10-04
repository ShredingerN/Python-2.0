'''
Создайте модуль и напишите в нём функцию, которая получает на вход дату в формате DD.MM.YYYY и возвращает истину,
если дата может существовать или ложь, если такая дата невозможна.
Для простоты договоримся, что год может быть в диапазоне [1, 9999].
И весь период действует григорианский календарь. Проверку года на високосность вынести в отдельную защищённую функцию.
'''
__all__ = ['check_date']


def check_date(date: str) -> bool:
    day, mounth, year = map(int, date.split('.'))
    if year % 4 == 0 or year % 100 != 0 and mounth == 2:
        return 1 <= day <= 29
    return 1 <= day <= 31 and 1 <= mounth <= 12 and 1 <= year <= 9999


# def _leap_year(year):
#     return year % 4 == 0 and year % 100 != 0


if __name__ == '__main__':
    date_to_prove = ('29.02.2999')
    print(check_date(date_to_prove))


def is_leap(year: int) -> bool:
    return not (year % 4 != 0 or year % 100 == 0 and year % 400 != 0)


def is_leap_year(full_date: str) -> bool:
    date, month, year = (int(item) for item in full_date.split('.'))
    if year < 1 or year > 9999 or month < 1 or month > 12 or date < 1 or date > 31:
        return False
    if month in (4, 6, 9, 11) and date > 30:
        return False
    if month == 2 and is_leap and date > 29:
        return False
    if month == 2 and not is_leap and date > 28:
        return False
    return True


if __name__ == "__main__":
    date_to_prove = '29.2.2021'
    print(is_leap_year(date_to_prove))