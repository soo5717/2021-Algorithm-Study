import sys
from collections import deque

def bfs(i, j):
  queue = deque()
  queue.append((i, j))

  dx = [0, 1, 0, -1]
  dy = [1, 0, -1, 0]
  
  area = 1
  while queue:
    x, y = queue.popleft()
    paper[x][y] = 0
    for d in range(4):
      nx = x + dx[d]
      ny = y + dy[d]
      # 유효한 좌표 확인 및 그림 여부 확인
      if 0<=nx<n and 0<=ny<m and paper[nx][ny]: # 조건이 모두 유효하다면
        paper[nx][ny] = 0  #방문 처리
        queue.append((nx, ny))
        area += 1
  return area

n, m = map(int, input().split())
paper = [list(map(int, sys.stdin.readline().split())) for _ in range(n)]

arts, max_area = 0, 0
for i in range(n):
  for j in range(m):
    if paper[i][j]: #0이 아닌 부분
      area = bfs(i, j) # 하나의 그림 탐색
      arts += 1 # 그림 개수 증가
      max_area = max(max_area, area)
      
print(arts)
print(max_area)
