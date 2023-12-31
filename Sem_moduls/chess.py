def is_attacking(q1, q2):
    return q1[0] == q2[0] or q1[1] == q2[1] or abs(q1[0] - q2[0]) == abs(q1[1] - q2[1])


def check_queens(queens):
    for i in range(len(queens)):
        for j in range(i + 1, len(queens)):
            if is_attacking(queens[i], queens[j]):
                return False
    return True


if __name__ == '__main__':
    print(check_queens(queens=[(1, 1), (2, 1), (3, 1), (4, 1), (5, 1), (6, 1), (7, 1), (8, 1)]))
    print(check_queens(queens=[(1, 1), (1, 2), (1, 3), (1, 4), (1, 5), (1, 6), (1, 7), (1, 8)]))
    print(check_queens(queens=[(1, 1), (2, 3), (3, 5), (4, 7), (5, 2), (6, 4), (7, 6), (8, 8)]))
    print(check_queens(queens=[(4, 4)]))
    print(check_queens(queens=[]))


