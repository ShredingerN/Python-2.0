# Напишите программу, которая получает целое число и возвращает его шестнадцатеричное строковое представление.
# Функцию hex используйте для проверки своего результата.

def num_hex(n):
    result = ''
    hex_str = '0123456789abcdef'
    check_num = hex(n)
    while n != 0:
        result = hex_str[n % 16] + result
        n //= 16
    if result == check_num[2:]:
        print(True)
        return result


num = int(input('Введите целое число: '))
print(num_hex(num))
