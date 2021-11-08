import sys

input = sys.stdin.readline


def is_bingo():
    bingo_count = 0
    diagonal_1, diagonal_2 = 0, 0
    for i in range(N):
        if not sum(bingo_matrix[i]):  # horizontal
            bingo_count += 1
        for j in range(N):
            if i == j:  # (0, 0) (1, 1) (2, 2) (3, 3) (4, 4)
                diagonal_1 += bingo_matrix[i][j]
            if j == N - 1 - i:  # (0, 4) (1, 3) (2, 2) (3, 1) (4, 0)
                diagonal_2 += bingo_matrix[i][j]
    for j in range(N):
        vertical = 0
        for i in range(N):
            vertical += bingo_matrix[i][j]
        if not vertical:
            bingo_count += 1

    if not diagonal_1:
        bingo_count += 1
    if not diagonal_2:
        bingo_count += 1

    if bingo_count >= 3:
        return True
    return False


if __name__ == "__main__":
    N = 5
    bingo_matrix, bingo_index = [], {}
    for r in range(N):
        bingo_matrix.append(list(map(int, input().split())))
        for c in range(N):
            bingo_index[bingo_matrix[r][c]] = (r, c)

    for i in range(N):
        input_numbers = list(map(int, input().split()))
        for j, input_number in enumerate(input_numbers):
            r, c = bingo_index[input_number]
            bingo_matrix[r][c] = 0  # check
            if is_bingo():
                print(i * N + (j + 1))
                exit()
