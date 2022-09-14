import sys
from collections import deque

# 상 하 좌 우
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]


def spread_water():
    global water_set
    new_water_set = set()

    for x, y in water_set:
        for d in range(4):
            nx = x + dx[d]
            ny = y + dy[d]

            if nx < 0 or nx >= r or ny < 0 or ny >= c:
                continue

            if matrix[nx][ny] == EMPTY:
                matrix[nx][ny] = WATER
                new_water_set.add((nx, ny))

    water_set = new_water_set


def bfs():
    queue = deque([start])
    matrix[start[0]][start[1]] = 0

    while queue:
        spread_water()

        for _ in range(len(queue)):
            x, y = queue.popleft()

            for d in range(4):
                nx = x + dx[d]
                ny = y + dy[d]

                if nx < 0 or nx >= r or ny < 0 or ny >= c:
                    continue

                if matrix[nx][ny] == EMPTY:
                    matrix[nx][ny] = matrix[x][y] + 1
                    queue.append((nx, ny))
                elif matrix[nx][ny] == BEAVER:
                    return matrix[x][y] + 1

    return "KAKTUS"


EMPTY, WATER, STONE = '.', '*', 'X'
BEAVER, HEDGEHOG = 'D', 'S'

r, c = map(int, input().split())

matrix = []
water_set = set()
start, end = (0, 0), (0, 0)

for i in range(r):
    matrix.append(list(sys.stdin.readline().strip()))

    for j, token in enumerate(matrix[i]):
        if token == BEAVER:
            end = (i, j)
        elif token == HEDGEHOG:
            start = (i, j)
        elif token == WATER:
            water_set.add((i, j))

print(bfs())

