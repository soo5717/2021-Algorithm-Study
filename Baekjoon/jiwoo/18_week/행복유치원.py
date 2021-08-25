N, K = map(int, input().split())
people = list(map(int, input().split()))

difference = []
for i in range(N-1):
	difference.append(people[i+1]-people[i])
difference.sort()

answer = 0
if K == N:
	print(answer)
else:
	for i in range(N-K):
		answer += difference[i]
	print(answer)