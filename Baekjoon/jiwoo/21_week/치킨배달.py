from itertools import combinations

N, M = map(int, input().split())

city = []
for i in range(N):
	city.append(list(map(int, input().split())))

homes = []
chickens = []
for i in range(N):
	for j in range(N):
		if city[i][j] == 1:
			homes.append((i,j))
		elif city[i][j] == 2:
			chickens.append((i,j))

pick_chicken = list(combinations(chickens, M))
distance = [0] * len(pick_chicken)

for home in homes:
	for j in range(len(pick_chicken)):
		d = 1e9
		for pick in pick_chicken[j]:
			temp = abs(home[0] - pick[0]) + abs(home[1] - pick[1])
			d = min(d, temp)
		distance[j] += d
print(min(distance))