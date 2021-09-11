N = int(input())

DP = [0, 1, 3]

for i in range(3, N+1):
    DP.append((DP[i-2] * 2) + DP[i-1])

print(DP[N] % 10007)