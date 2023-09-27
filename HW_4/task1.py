# Напишите функцию для транспонирования матрицы.

def trans_matrix(mat: list) -> list[int]:
    return list(map(list, zip(*mat)))


matrix = [[1, 2, 3, 20],
          [4, 5, 6, 21],
          [7, 8, 9, 22]]

new_matrix = trans_matrix(matrix)

print(*matrix, sep='\n')
print()
print(*new_matrix, sep='\n')