import sys
from collections import deque

input = lambda: sys.stdin.readline()

EMPTY, SNAKE, APPLE = 0, 1, 2
LEFT, RIGHT = 'L', 'D'

# 오른쪽, 아래, 왼쪽, 위 (시계 방향)
dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]


def rotate(time, direction):
    if time not in rotations:
        return direction

    if rotations[time] == RIGHT:
        return (direction + 1) % 4

    if rotations[time] == LEFT:
        return 3 if not direction else direction - 1


def move():
    time, direction = 0, 0

    head_x, head_y = 0, 0
    snakes = deque([(head_x, head_y)])

    while True:
        direction = rotate(time, direction)
        nx = head_x + dx[direction]
        ny = head_y + dy[direction]

        time += 1

        if nx < 0 or nx >= n or ny < 0 or ny >= n:
            break

        if matrix[nx][ny] == SNAKE:
            break

        if matrix[nx][ny] != APPLE:
            tail_x, tail_y = snakes.popleft()
            matrix[tail_x][tail_y] = EMPTY

        matrix[nx][ny] = SNAKE
        snakes.append((nx, ny))
        head_x, head_y = nx, ny

    return time


n = int(input())

rotations = {}
matrix = [[EMPTY] * n for _ in range(n)]

for _ in range(int(input())):
    row, col = map(int, input().split())
    matrix[row - 1][col - 1] = APPLE

for _ in range(int(input())):
    second, rotation = input().split()
    rotations[int(second)] = rotation

print(move())
