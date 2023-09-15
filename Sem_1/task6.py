# Напишите программу, которая получает целое число и возвращает его двоичное, восьмеричное строковое представление.
# Функции bin и oct используйте для проверки своего результата.

number = 50
b = oct(number)
result = ""
while number > 0:
    result = str(number % 8) + result
    number = number // 8
print(result)
if result == b[2:]:
    print(True)
