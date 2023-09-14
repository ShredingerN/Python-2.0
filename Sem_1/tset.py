num = 2 + 2 * 2
digit = 36 // 6 #целочисленное деление
digit1 = 36 / 6 #вещественный тип на выходе
print(num == digit, id(num), id(digit))
print(num is digit, id(num), id(digit))
print(num is digit1,id(num), id(digit1))

user = input("Enter string: ")
print(type(user), id(user), hash(user))
