from chess import check_queens
from random import sample


def generate_boards():
    board_list = []

    while len(board_list) < 4:
        queens = sample(range(1, 9), 8)  # Генерируем уникальные числа от 1 до 8
        queens = [(i, queens[i - 1]) for i in range(1, 9)]
        if check_queens(queens):
            board_list.append(queens)

    return board_list


if __name__ == '__main__':
    print(generate_boards())

# def generate_board():
#     # Генерируем случайную доску
#     board = []
#
#     for i in range(1, 8 + 1):
#         queen = (i, random.randint(1, 8))
#         board.append(queen)
#     return board
#
#
# def is_attacking(q1, q2):
#     # Проверяем, бьют ли ферзи друг друга
#     return q1[0] == q2[0] or q1[1] == q2[1] or abs(q1[0] - q2[0]) == abs(q1[1] - q2[1])
#
#
# def check_queens(queens):
#     # Проверяем все возможные пары ферзей
#     for q1, q2 in combinations(queens, 2):
#         if is_attacking(q1, q2):
#             return False
#     return True
#
#
# def generate_boards1():
#     # Генерируем доски, пока не получим 4 успешные расстановки
#     count = 0
#     board_list = []
#     while count < 4:
#         board = generate_board()
#         if check_queens(board):
#             count += 1
#             board_list.append(board)
#     return board_list
#
#
# if __name__ == '__main__':
#     print(generate_boards1())
