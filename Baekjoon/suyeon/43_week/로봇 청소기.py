import sys

input = sys.stdin.readline

EMPTY, WALL, CLEAN = 0, 1, 2

# 북(상) 동(좌) 남(하) 서(우) - 반시계 방향
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

n, m = map(int, input().split())
x, y, d = map(int, input().split())

matrix = [list(map(int, input().split()))for _ in range(n)]

answer = 1
matrix[x][y] = CLEAN

while True:
  check = False 
  
  for _ in range(4):
    d = (d + 3) % 4
    nx = x + dx[d]
    ny = y + dy[d]

    if 0 <= nx < n and 0 <= ny < m and matrix[nx][ny] == EMPTY:
      matrix[nx][ny] = CLEAN
      answer += 1
      
      check = True
      x, y = nx, ny
      
      break

  if not check:
    nx = x - dx[d]
    ny = y - dy[d]
  
    if 0 <= nx < n and 0 <= ny < m and matrix[nx][ny] == WALL:
        break
    x, y = nx, ny

print(answer)