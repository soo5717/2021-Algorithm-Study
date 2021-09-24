import sys

input = sys.stdin.readline

N = int(input())
people_train = [0] + list(map(int, input().split()))
max_train = int(input())

for i in range(1, len(people_train)):
	people_train[i] += people_train[i-1]

dp = [[0] * (N+1) for _ in range(4)]
for i in range(1, 4):
	for j in range(i * max_train, N+1):
		if i == 1:
			dp[i][j] = max(dp[i][j-1], people_train[j] - people_train[j-max_train])
		else:
			dp[i][j] = max(dp[i][j-1], dp[i-1][j-max_train] + people_train[j] - people_train[j-max_train])
print(dp[3][N])