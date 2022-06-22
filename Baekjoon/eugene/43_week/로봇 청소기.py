import sys

n, m = map(int, input().split())
r, c, d = map(int, input().split())

map = [list(map(int, sys.stdin.readline().split())) for _ in range(n)]
clean = [[0]* m for _ in range(n)]


dx = [-1,0,1,0]
dy = [0,1,0,-1]

cnt = 1
clean[r][c] = 1 # 청소한 상태 1, 청소하지 않으면 0

while True:
  # 방향 초기화(종료조건)
  direction = 0 

  #2-a
  for _ in range(4):
    nx = r + dx[(3+d)%4]
    ny = c + dy[(3+d)%4]
    d = (3+d)%4

    if 0 <= nx < n and 0 <= ny < m and map[nx][ny] == 0 and clean[nx][ny] == 0:
      clean[nx][ny] = 1
      cnt += 1
      direction = 1 # 청소했으므로 2a-4번 종료 조건 피하기
      r, c = nx, ny
      break

  #2-a를 4번 다 돌았는데 direction이 여전히 0이면 
  if direction == 0:
    r, c = r-dx[d],c-dy[d] # 한칸 후진 해보고
    if map[r][c] == 1: # 벽이면 작동 중지
      break
    
    
print(cnt)  
