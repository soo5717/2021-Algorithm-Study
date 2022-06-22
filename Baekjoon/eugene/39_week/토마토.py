import sys
from collections import deque

m, n, h = map(int, input().split())
farm = [[list(map(int,sys.stdin.readline().split())) for _ in range(n)] for _ in range(h)]

day = 0
dx = [0, 0, 0, 0, -1, 1]
dy = [0, 0, -1, 1, 0, 0]
dz = [-1, 1, 0, 0, 0, 0]

queue = deque()
for i in range(h):
  for j in range(n):
    for k in range(m):
      if farm[i][j][k] == 1:
        queue.append((i, j, k))

while queue:
  day += 1
  for _ in range(len(queue)):
    x, y, z = queue.popleft()
    for i in range(6):
      nx = x + dx[i]
      ny = y + dy[i]
      nz = z + dz[i]

      if 0 <= nx < h and 0 <= ny < n and 0 <= nz < m and farm[nx][ny][nz] == 0:
        farm[nx][ny][nz] = 1
        queue.append((nx, ny, nz))
      else:
        continue

for i in range(h):
  for j in range(n):
    for k in range(m):
      if not farm[i][j][k]:
        print(-1)
        exit(0)
print(day-1)
