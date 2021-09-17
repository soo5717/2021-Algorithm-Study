import sys

input = sys.stdin.readline


def get_max_passenger():
    dp = [[0] * (n + 1) for _ in range(4)]
    for i in range(1, 4):
        for j in range(i * max_transit, n + 1):
            if i == 1:
                dp[i][j] = max(dp[i][j - 1], trains[j] - trains[j - max_transit])
            else:
                dp[i][j] = max(dp[i][j - 1], dp[i - 1][j - max_transit] + trains[j] - trains[j - max_transit])
    return dp[3][n]


if __name__ == '__main__':
    n = int(input())
    trains = [0] + list(map(int, input().split()))
    max_transit = int(input())

    for idx in range(1, len(trains)):
        trains[idx] += trains[idx - 1]
    print(get_max_passenger())
