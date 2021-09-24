import sys
from itertools import combinations

input = sys.stdin.readline


if __name__ == "__main__":
    N, M = map(int, input().split())
    matrix = [list(map(int, input().split())) for _ in range(N)]

    home_set, chicken_set = set(), set()
    for i in range(N):
        for j in range(N):
            if matrix[i][j] == 1:
                home_set.add((i, j))
            elif matrix[i][j] == 2:
                chicken_set.add((i, j))

    answer = int(1e9)
    for chicken_list in combinations(chicken_set, M):
        min_sum = 0
        for home_i, home_j in home_set:
            min_sum += min([abs(home_i - chicken_i) + abs(home_j - chicken_j) for chicken_i, chicken_j in chicken_list])
            if answer <= min_sum:
                break
        if min_sum < answer:
            answer = min_sum
    print(answer)
