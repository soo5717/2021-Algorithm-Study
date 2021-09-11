N = int(input())

dp = [0, 1, 3]

for i in range(3, N+1):
    dp.append((dp[i-2] * 2) + dp[i-1])

print(dp[N] % 10007)