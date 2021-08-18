N = int(input())

meeting = [list(map(int, input().split())) for i in range(N)]
dp = [0 for i in range(N+1)]

for i in range(N-1, -1, -1):
	if i + meeting[i][0] > N:
		dp[i] = dp[i+1]
	else:
		dp[i] = max(meeting[i][1] + dp[i+meeting[i][0]], dp[i+1])

print(dp[0])