# Создайте словарь со списком вещей для похода в качестве ключа и их массой в качестве значения. Определите какие вещи
# влезут в рюкзак передав его максимальную грузоподъёмность. Достаточно вернуть один допустимый вариант.
# *Верните все возможные варианты комплектации рюкзака.

from itertools import combinations


def backpack_things(things, capacity):
    packaging = []
    for key, value in things.items():
        if value <= capacity:
            capacity -= value
            # print(capacity)
            packaging.append((key, value))
    return packaging


def all_comb(things, capacity):
    temp_list = []
    for key, value in things.items():
        temp_list.append((key, value))
    # print(temp_list)
    all_combinations = []
    for i in range(1, len(temp_list) + 1):
        combinations_set = combinations(temp_list, i)
        for combination in combinations_set:
            total_weight = 0
            for _, weight in combination:
                total_weight += weight
            if total_weight <= capacity:
                variant = []
                for name, _ in combination:
                    variant.append(name)
                    # print(variant)
                all_combinations.append(variant)
                # print(all_combinations)
    return all_combinations


things = {'котелок': 2,
          'тушенка': 1.5,
          'топор': 2,
          'фонарь': 1,
          'вода': 1.5,
          'палатка': 5,
          'мангал': 3,
          'куртка': 1,
          'спальный мешок': 2,
          'кружка': 0.3,
          'гречка': 1,
          'косметичка': 1.5
          }
# один возможный вариант
capacity = int(input('Введите грузоподъемность рюкзака: '))
print(backpack_things(things, capacity))
# все возможные варианты
all_variants = all_comb(things, capacity)
print(f'Варианты комплектации вещей для рюкзака, вместимостью {capacity} кг')
for i, variant in enumerate(all_variants, start=1):
    print(f'{i}: {variant}')
