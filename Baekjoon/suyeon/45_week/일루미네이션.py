import sys
from collections import deque

WALL, EMPTY = 1, 0

input = sys.stdin.readline

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]


def count_light(x, y):
    count = 0

    for d in range(4):
        nx, ny = x + dx[d], y + dy[d]

        if matrix[nx][ny] == 2:
            count += 1

    return count


def spread_bfs():
    queue = deque([(0, 0)])
    matrix[0][0] = 2

    while queue:
        x, y = queue.popleft()

        for d in range(4):
            nx, ny = x + dx[d], y + dy[d]

            if nx < 0 or nx >= matrix_h or ny < 0 or ny >= matrix_w:
                continue

            if matrix[nx][ny] == EMPTY:
                matrix[nx][ny] = 2
                queue.append((nx, ny))


w, h = map(int, input().split())

walls = set()
matrix = [[0] * (w * 2 + 3) for _ in range(h + 2)]
matrix_h, matrix_w = len(matrix), len(matrix[0])

for i in range(h):
    row = i + 1
    col = 1 if i % 2 else 2

    for input_type in map(int, input().split()):
        if input_type == WALL:
            matrix[row][col] = WALL
            matrix[row][col + 1] = WALL
            walls.update([(row, col), (row, col + 1)])

        col += 2

spread_bfs()

answer = 0
for row, col in walls:
    if matrix[row][col] == WALL:
        answer += count_light(row, col)

print(answer)
