# import sys
#
# t = "123445567"
# print(str.isdecimal(t))
# # print(bin(t))
# # print(oct(t))
# # print(hex(t))
#
# print(str.isascii(t))
# print(str.isalnum(t))

data = [25, -42, 146, 73, -100, 12]
print(list(map(str, data)))
# переделывает применяем - ко всем числам в списке и возвращаем макс
print(max(data, key=lambda x: -x))
#х - ключ-значение, убираем даденр методы
print(*filter(lambda x: not x[0].startswith('__'),globals().items()))