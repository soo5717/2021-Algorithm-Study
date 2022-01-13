import sys
from itertools import combinations
from copy import deepcopy

input = sys.stdin.readline

EMPTY, WALL, VIRUS = 0, 1, 2
MAX_WALL = 3

dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]


def spread_virus(matrix, x, y):
    global empty_space_count

    for i in range(4):
        nx, ny = x + dx[i], y + dy[i]

        if nx < 0 or nx >= N or ny < 0 or ny >= M:
            continue
        if matrix[nx][ny] == EMPTY:
            matrix[nx][ny] = VIRUS
            empty_space_count -= 1
            spread_virus(matrix, nx, ny)


if __name__ == "__main__":
    N, M = map(int, input().split())

    lab_matrix, empty_space, virus_space = [], [], []
    for i in range(N):
        temp = list(map(int, input().split()))

        for j in range(M):
            if temp[j] == EMPTY:
                empty_space.append((i, j))
            elif temp[j] == VIRUS:
                virus_space.append((i, j))

        lab_matrix.append(temp)

    safe_space_count = 0
    for first, second, third in combinations(empty_space, MAX_WALL):
        copy_lab_matrix = deepcopy(lab_matrix)

        copy_lab_matrix[first[0]][first[1]] = WALL
        copy_lab_matrix[second[0]][second[1]] = WALL
        copy_lab_matrix[third[0]][third[1]] = WALL

        empty_space_count = len(empty_space) - 3
        for r, c in virus_space:
            spread_virus(copy_lab_matrix, r, c)

        safe_space_count = max(empty_space_count, safe_space_count)

    print(safe_space_count)
