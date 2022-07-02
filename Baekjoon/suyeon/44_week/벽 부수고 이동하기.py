import sys
from collections import deque

input = sys.stdin.readline

EMPTY, WALL = 0, 1

dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]

def bfs():
  queue = deque()
  queue.append((0, 0, 0))
  visited[0][0][0] = 1
    
  while queue:
    x, y, w = queue.popleft()
    
    if x == n - 1 and y == m - 1:
      return visited[x][y][w]
            
    for i in range(4):
      nx = x + dx[i]
      ny = y + dy[i]
            
      if nx < 0 or nx >= n or ny < 0 or ny >= m:
        continue
            
      if matrix[nx][ny] == EMPTY  and visited[nx][ny][w] == 0:
        visited[nx][ny][w] = visited[x][y][w] + 1
        queue.append((nx, ny, w))
      elif matrix[nx][ny] == WALL and w == 0:
        visited[nx][ny][1] = visited[x][y][w] + 1
        queue.append((nx, ny, 1))
    
  return -1


n, m = map(int, input().split())
matrix = [list(map(int, input().strip())) for _ in range(n)]
visited = [[[0, 0] for _ in range(m)] for _ in range(n)]

print(bfs())