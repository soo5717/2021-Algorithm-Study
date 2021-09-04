import sys

input = sys.stdin.readline
move = [(-1, 0), (0, 1), (1, 0), (0, -1)]

def get_dot():
    sea_point = []
    for i in range(R):
        for j in range(C):
            if sea_map[i][j] == '.':
                continue

            count = 0
            for mx, my in move:
                nx = i + mx
                ny = j + my

                if nx < 0 or nx >= R or ny < 0 or ny >= C:
                    count += 1
                    continue

                if sea_map[nx][ny] == '.':
                    count += 1

            if count >= 3:
                sea_point.append((i, j))
    return sea_point

R, C = map(int, input().split())
sea_map = [list(input().strip()) for _ in range(R)]

for x, y in get_dot():
    sea_map[x][y] = '.'

start_row, end_row = R-1, 0
start_col, end_col = C-1, 0
for i in range(R):
	for j in range(C):
		if sea_map[i][j] == 'X':
			if start_row > i:
				start_row = i
			if end_row < i:
				end_row = i
			if start_col > j:
				start_col = j
			if end_col < j:
				end_col = j

for l in sea_map[start_row:end_row+1]:
    print(''.join(l[start_col:end_col+1]))