# Создайте функцию для сортировки файлов по директориям:
# видео,
# изображения,
# текст и т.п.
# Каждая группа включает файлы с несколькими расширениями.
# В исходной папке должны остаться только те файлы, которые не подошли для сортировки.


import os
import pathlib


# def sort_file1(path):
#     os.chdir(path)
#     ext = {}
#     for i in path.iterdir():
#         if i.is_file():
#             ext[i.suffix] = ext.get(i.suffix, []) + [i]
#     for key, value in ext.items():
#         os.mkdir(key)
#         for file in value:
#             file.replace(path / key / file.name)
#
#
# sort_file1(pathlib.Path(r"C:\Users\jo467\Downloads\Тестировщик\Python 2.0\Sem7_MOD\test_sort_file")

def sort_file(path):
    os.chdir(path)
    files = os.listdir()
    ext = {}
    for i in files:
        *_, extension = i.split('.')
        ext[extension] = ext.get(extension, []) + [i]
    for key, value in ext.items():
        os.mkdir(key)
        for i in value:
            os.replace(i, f'{key}\\{i}')


sort_file(r"C:\Users\jo467\Downloads\Тестировщик\Python 2.0\Sem7_MOD\test_sort_file")
