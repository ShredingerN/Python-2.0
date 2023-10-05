# Вспоминаем задачу 3 из прошлого семинара. Мы сформировали текстовый файл с псевдо именами и произведением чисел.
# Напишите функцию, которая создаёт из созданного ранее файла новый с данными в формате JSON.
# Имена пишите с большой буквы. Каждую пару сохраняйте с новой строки.

import json


def to_json(old_f, new_f):
    with open(old_f, 'r') as f:
        data = dict({i.split()[0].capitalize(): float(i.split()[1]) for i in f.read().split('\n')})
        print(data)
    with open(new_f, 'w') as new_f:
        json.dump(data, new_f, indent=4)


to_json(r'C:\Users\jo467\Downloads\Тестировщик\Python 2.0\Seminars\output.txt', 'to_json.json')
