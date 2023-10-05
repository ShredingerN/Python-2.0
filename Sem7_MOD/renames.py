# Напишите функцию группового переименования файлов. Она должна:
# - принимать параметр желаемое конечное имя файлов. При переименовании в конце имени добавляется порядковый номер.
# - принимать параметр количество цифр в порядковом номере.
# - принимать параметр расширение исходного файла. Переименование должно работать только для этих файлов внутри каталога.
# - принимать параметр расширение конечного файла.
# - принимать диапазон сохраняемого оригинального имени.
#
# Например для диапазона [3, 6] берутся буквы с 3 по 6 из исходного имени файла.
# К ним прибавляется желаемое конечное имя, если оно передано. Далее счётчик файлов и расширение.

import os
from createfiles import create_files

import os


def rename_files(directory, desired_name, num_digits, source_extension, target_extension, name_range=None):
    # Получаем список файлов в указанной директории
    files = os.listdir(directory)

    # Фильтруем файлы по расширению
    files = [file for file in files if file.endswith(source_extension)]

    # Определяем начальное значение счетчика
    counter = 1

    # Перебираем файлы
    for file in files:
        # Определяем оригинальное имя файла в соответствии с диапазоном
        original_name = file[name_range[0] - 1:name_range[1]]

        # Формируем новое имя файла
        new_name = f"{desired_name}{original_name}_{counter:0{num_digits}d}.{target_extension}"

        # Составляем полные пути к исходному и целевому файлам
        source_path = os.path.join(directory, file)
        target_path = os.path.join(directory, new_name)

        # Переименовываем файл
        os.rename(source_path, target_path)

        # Увеличиваем счетчик
        counter += 1


# Пример использования

desired_name = "new"
num_digits = 4
source_extension = ".txt"
target_extension = "csv"
name_range = (3, 6)



create_files(r'C:\Users\jo467\Downloads\Тестировщик\Python 2.0\Sem7_MOD\test_rename', '.txt', 2)
create_files(r'C:\Users\jo467\Downloads\Тестировщик\Python 2.0\Sem7_MOD\test_rename', '.json', 2)
create_files(r'C:\Users\jo467\Downloads\Тестировщик\Python 2.0\Sem7_MOD\test_rename', '.jpeg', 2)

rename_files(r'C:\Users\jo467\Downloads\Тестировщик\Python 2.0\Sem7_MOD\test_rename', desired_name, num_digits, source_extension, target_extension, name_range)

