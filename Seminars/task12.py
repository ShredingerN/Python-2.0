# Три друга взяли вещи в поход. Сформируйте словарь, где ключ - имя друга, а значение - кортеж вещей. Ответьте на вопросы:
# какие вещи взяли все три друга
# какие вещи уникальны, есть только у одного друга
# какие вещи есть у всех друзей кроме одного и имя того, у кого данная вещь отсутствует
# Для решения используйте операции с множествами. Код должен расширяться на любое большее количество друзей.
hike = {
    'Aaz': ("спальник", "дрова", "топор"),
    'Skeeve': ("спальник", "спички", "вода", "еда"),
    'Tananda': ("вода", "косметичка"),
    'Vanya': ("вода", "спички", "косметичка"),
}

result = set()
for i in hike.values():
    if result == set():
        result = set(i)
    else:
        result = result & set(i)
print(result)
print()

only = set()
for i in hike.values():
    only = set(i)
    for j in hike.values():
        if i == j:
            continue
        else:
            only -= set(j)
    print(only)
print()


for name, i in hike.items():
    uniq = None
    for j in hike.values():
        if i == j:
            continue
        elif not uniq and uniq != set():
            uniq = set(j)
        else:
            uniq &= set(j)
    print(name, uniq - set(i))

