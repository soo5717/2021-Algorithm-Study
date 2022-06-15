import sys
from collections import deque

input = sys.stdin.readline

# 상, 하, 좌, 우
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]


def bfs(x, y):
  queue = deque()
  queue.append((x, y))

  count = 0
  
  while queue:
    x, y = queue.popleft()

    if matrix[x][y] != 1:
      continue

    count += 1
    matrix[x][y] = 0
    
    for i in range(4):
      nx = x + dx[i]
      ny = y + dy[i]

      if nx < 0 or nx >= n or ny < 0 or ny >= m:
        continue

      if matrix[nx][ny] == 1:
        queue.append((nx, ny))

  return count
    

n, m = map(int, input().split())

matrix = [list(map(int, input().split())) for _ in range(n)]

picture = []

for x in range(n):
  for y in range(m):
    if matrix[x][y] == 1:
      picture.append(bfs(x, y))

print(len(picture))
print(max(picture) if len(picture) else 0)