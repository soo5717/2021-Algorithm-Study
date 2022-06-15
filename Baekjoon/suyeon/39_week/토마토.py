import sys
from collections import deque

input = sys.stdin.readline

# -1 토마토 없음 / 0 안 익은 토마토 / 1 익은 토마토

# 위, 아래, 상, 하, 좌, 우
dz = [-1, 1, 0, 0, 0, 0]
dy = [0, 0, 0, 0, -1, 1]
dx = [0, 0, -1, 1, 0, 0]

def bfs():
  while queue:
    z, y, x = queue.popleft()

    for i in range(6):
      nz = z + dz[i]
      ny = y + dy[i]
      nx = x + dx[i]

      if nz < 0 or ny < 0 or nx < 0 or nz >= h or ny >= n or nx >= m:
        continue

      if dimen_3[nz][ny][nx] == -1:
        continue

      if dimen_3[nz][ny][nx] == 0:
        queue.append((nz, ny, nx))
        dimen_3[nz][ny][nx] = dimen_3[z][y][x] + 1

m, n, h = map(int, input().split())

def get_min_day():
  max_day = -1
  
  for z in range(h):
    for y in range(n):
      for x in range(m):
        if dimen_3[z][y][x] == 0:
          return -1

        if dimen_3[z][y][x] > max_day:
          max_day = dimen_3[z][y][x]

  if max_day == 1:
    return 0
    
  return max_day - 1

dimen_3 = []
queue = deque([])

for z in range(h):
  dimen_2 = []
  for y in range(n):
    dimen_1 = list(map(int, input().split()))
    for x in range(m):
      if dimen_1[x] == 1:
        queue.append((z, y, x))
    dimen_2.append(dimen_1)
  dimen_3.append(dimen_2)

bfs()
print(get_min_day())