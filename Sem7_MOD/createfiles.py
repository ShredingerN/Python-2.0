# Создайте функцию, которая создаёт файлы с указанным расширением. Функция принимает следующие параметры:
# расширение
# минимальная длина случайно сгенерированного имени, по умолчанию 6
# максимальная длина случайно сгенерированного имени, по умолчанию 30
# минимальное число случайных байт, записанных в файл, по умолчанию 256
# максимальное число случайных байт, записанных в файл, по умолчанию 4096
# количество файлов, по умолчанию 42
# Имя файла и его размер должны быть в рамках переданного диапазона.

from pseudo import rnd_name
from random import randint
import os


def create_files(directory, extension, qty_file=42, max_len_name=30, min_len_name=6, min_byte=256, max_byte=4096):
    for _ in range(qty_file):
        file_name = rnd_name() + extension
        file_path = os.path.join(directory, file_name)
        with open(file_path, 'w') as f:
            f.write(str(bytes([randint(0, 255) for _ in range(randint(min_byte, max_byte))])))


if __name__ == '__main__':
    create_files(r'C:\Users\jo467\Downloads\Тестировщик\Python 2.0\Sem7_MOD\test_rename', '.txt', 5)
