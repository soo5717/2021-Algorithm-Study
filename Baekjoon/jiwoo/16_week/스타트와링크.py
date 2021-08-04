from itertools import combinations

N = int(input())
soccer_map = [0 for i in range(N+1)]
for i in range(N):
    soccer_map[i] = list(map(int, input().split()))

teams = list(combinations(range(1, N+1), N//2))

dif_score = []

for i in range(len(teams)//2):
	start_score = 0
	link_score = 0
	start_team = teams[i]
	link_team = teams[len(teams)-i-1]
	
	start_team_ = list(combinations(start_team, 2))
	link_team_ = list(combinations(link_team, 2))
	for a, b in start_team_:
		start_score += (soccer_map[a-1][b-1] + soccer_map[b-1][a-1])
	for a, b in link_team_:
		link_score += (soccer_map[a-1][b-1] + soccer_map[b-1][a-1])
	dif_score.append(abs(start_score-link_score))

print(min(dif_score))