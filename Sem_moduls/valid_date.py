'''
Создайте модуль и напишите в нём функцию, которая получает на вход дату в формате DD.MM.YYYY и возвращает истину,
если дата может существовать или ложь, если такая дата невозможна.
Для простоты договоримся, что год может быть в диапазоне [1, 9999].
И весь период действует григорианский календарь. Проверку года на високосность вынести в отдельную защищённую функцию.
'''
__all__ = ['check_date']

def check_date(date: str) -> bool:
    day, mounth, year = map(int, date.split('.'))
    if _leap_year(year) and mounth == 2:
        return 1 <= day <= 29
    return 1 <= day <= 31 and 1 <= mounth <= 12 and 1 <= year <= 9999


def _leap_year(year):
    return year % 4 == 0 and year % 100 != 0


if __name__ == '__main__':
    print(check_date(input()))
