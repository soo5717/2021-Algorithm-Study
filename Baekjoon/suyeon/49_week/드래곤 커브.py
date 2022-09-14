import sys

MATRIX_SIZE = 101

# 우0 상1 좌2 하3
dx = [1, 0, -1, 0]
dy = [0, -1, 0, 1]


def draw_dragon_curve(info):
    start_x, start_y, direction, generation = info

    move = [direction]
    for _ in range(generation):
        move.extend([(d + 1) % 4 for d in move[::-1]])

    nx, ny = start_x, start_y
    matrix[nx][ny] = True

    for d in move:
        nx, ny = nx + dx[d], ny + dy[d]
        matrix[nx][ny] = True


def get_rectangle_count():
    count = 0
    
    for i in range(1, MATRIX_SIZE):
        for j in range(1, MATRIX_SIZE):
            if matrix[i - 1][j - 1] and matrix[i - 1][j] and matrix[i][j - 1] and matrix[i][j]:
                count += 1

    return count


N = int(input())
matrix = [[False] * MATRIX_SIZE for _ in range(MATRIX_SIZE)]

for _ in range(N):
    draw_dragon_curve(map(int, sys.stdin.readline().split()))

print(get_rectangle_count())

