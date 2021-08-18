import sys

input = sys.stdin.readline

n = int(input())
schedule = [tuple(map(int, input().split())) for _ in range(n)]

answer = 0
dp = [0] * (n + 1)
for i in range(n - 1, -1, -1):
    term, price = schedule[i]
    if i + term <= n:
        answer = max(price + dp[i + term], answer)
    dp[i] = answer

print(answer)