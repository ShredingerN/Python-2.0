# Дан список повторяющихся элементов. Вернуть список с дублирующимися элементами.
# В результирующем списке не должно быть дубликатов.

a = [3, 5, 'a', 'v', 5, 7, 4, 'v', 'b', 4, 8, 8, 9, 2, 2, 1, 'v']
# a = [1, 2, 3, 4, 5, 6]

res = []
for el in a:
    count_el = a.count(el)
    if count_el > 1 and el not in res:
        res.append(el)
print(res)

res_set = set()
for el in a:
    count_el = a.count(el)
    if count_el > 1:
        res_set.add(el)
print(list(res_set))
