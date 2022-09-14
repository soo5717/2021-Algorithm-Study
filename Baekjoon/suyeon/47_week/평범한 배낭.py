import sys

n, k = map(int, input().split())
dp = [0] * (k + 1)

for _ in range(n):
    weight, value = map(int, sys.stdin.readline().split())

    for i in range(k, weight - 1, -1):
        dp[i] = max(value + dp[i - weight], dp[i])

print(dp[-1])

