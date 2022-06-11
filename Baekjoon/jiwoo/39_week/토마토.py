from collections import deque

M, N, H = map(int, input().split())
box = [[list(map(int, input().split())) for i in range(N)] for j in range(H)]

dx = [1, -1, 0, 0, 0, 0]
dy = [0, 0, -1, 1, 0, 0]
dz = [0, 0, 0, 0, -1, 1]

def bfs():
    while queue:
        z, x, y = queue.popleft()
        for i in range(6):
            a = x + dx[i]
            b = y + dy[i]
            c = z + dz[i]

            if 0 <= a < N and 0 <= b < M and 0 <= c < H:
                if box[c][a][b] == 0:
                    queue.append([c, a, b])
                    box[c][a][b] = box[z][x][y] + 1
queue = deque()
for i in range(H):
    for j in range(N):
        for k in range(M):
            if box[i][j][k] == 1:
                queue.append([i, j, k])

bfs()
z = 1
result = -1

for i in box:
    for j in i:
        for k in j:
            if k == 0:
                z = 0
            result = max(result, k)
     
if z == 0:
    print(-1)
elif result == 1:
    print(0)
else:
    print(result-1)