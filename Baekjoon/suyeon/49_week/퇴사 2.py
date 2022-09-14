import sys

N = int(input())
matrix = [tuple(map(int, sys.stdin.readline().split())) for _ in range(N)]

max_price = 0
dp = [0] * (N + 1)

for day in range(N - 1, -1, -1):
    term, price = matrix[day]

    if day + term <= N:
        max_price = max(price + dp[day + term], max_price)

    dp[day] = max_price

print(max_price)

