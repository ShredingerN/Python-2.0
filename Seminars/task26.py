# Напишите декоратор, который сохраняет в json файл параметры декорируемой функции и результат, который она возвращает.
# При повторном вызове файл должен расширяться, а не перезаписываться.
# Каждый ключевой параметр сохраните как отдельный ключ json словаря.
# Для декорирования напишите функцию, которая может принимать как позиционные, так и ключевые аргументы.
# Имя файла должно совпадать с именем декорируемой функции.

import json


def func_dec(func):
    try:
        with open(func.__name__ + ".json", "r") as f:
            data = json.load(f)
    except FileNotFoundError:
        data = []

    def wrapper(*args, **kwargs):
        result = func(*args, **kwargs)
        data.append({"args": args, **kwargs, "result": result})
        with open(func.__name__ + ".json", "w") as f:
            json.dump(data, f, indent=2)
        return result

    return wrapper


@func_dec
def sum_func(a, b, *args, **kwargs):
    return a + b


if __name__ == '__main__':
    print(sum_func(13, 14, 15, t=7, y=7, o=44, r=6))
