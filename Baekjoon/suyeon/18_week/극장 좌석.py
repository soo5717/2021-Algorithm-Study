import sys

input = sys.stdin.readline

N, M = int(input()), int(input())
dp = [1] * (N + 1)
for i in range(2, N + 1):
    dp[i] = dp[i - 1] + dp[i - 2]

prev_num, answer = 0, 1
for _ in range(M):
    current_num = int(input())
    answer *= dp[current_num - prev_num - 1]
    prev_num = current_num
answer *= dp[N - prev_num]

print(answer)