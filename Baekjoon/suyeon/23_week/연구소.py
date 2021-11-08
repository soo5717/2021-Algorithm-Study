import sys
from itertools import combinations
from copy import deepcopy

input = sys.stdin.readline

EMPTY, WALL, VIRUS = 0, 1, 2
MAX_WALL = 3

dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]


def spread_virus(matrix, x, y):
    for i in range(4):
        nx, ny = x + dx[i], y + dy[i]

        if nx < 0 or nx >= N or ny < 0 or ny >= M:
            continue
        if matrix[nx][ny] == EMPTY:
            matrix[nx][ny] = VIRUS
            spread_virus(matrix, nx, ny)


def get_safe_space_count(matrix):
    count = 0
    for i in range(N):
        for j in range(M):
            if matrix[i][j] == EMPTY:
                count += 1
    return count


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

        for r, c in virus_space:
            spread_virus(copy_lab_matrix, r, c)

        safe_space_count = max(get_safe_space_count(copy_lab_matrix), safe_space_count)

    print(safe_space_count)
