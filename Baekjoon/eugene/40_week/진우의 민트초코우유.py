import sys

def dfs(x, y, hp):
  for mint_x, mint_y in mint:
    if map_info[mint_x][mint_y] == 2:
      temp = abs(mint_x - x) + abs(mint_y, y)
      if temp <= hp:
        map_info[mint_x][mint_y] = 0
        dfs(mint_x, mint_y, hp - temp + h)
        map_info[mint_x][mint_y] = 2

  if abs(x - home_x) + abs(y, home_y) <= hp:
    result_milk = max(result_milk, )


n, m, h = map(int, input().split())
map_info = [list(map(int, sys.stdin.readline().split())) for _ in range(n)]

mint = []
result_milk = 0

for i in range(n):
  for j in range(n):
    if map_info[i][j] == 1:
      home_x, home_y = i, j
    elif map_info[i][j] == 2:
      mint.append((i, j))

dfs(home_x, home_y, m)
