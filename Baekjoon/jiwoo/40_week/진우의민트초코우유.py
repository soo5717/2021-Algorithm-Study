import sys
readline = lambda: sys.stdin.readline().strip()

def dfs(x, y, HP, mint):
    global result
        
    for nx, ny in mint_milks:
        if village[nx][ny] == 2:
            distance = abs(nx - x) + abs(ny - y)
            if distance <= HP:
                village[nx][ny] = 0
                dfs(nx, ny, HP + H - distance, mint + 1)
                village[nx][ny] = 2
    if abs(x - a) + abs(y - b) <= HP:
        result = max(result, mint)

N, M, H = map(int, readline().split())
village = [list(map(int, readline().split())) for _ in range(N)]

mint_milks = []
a, b = 0, 0

for i in range(N):
    for j in range(N):
        if village[i][j] == 1:
            a, b = i, j
        if village[i][j] == 2:
            mint_milks.append((i, j))

result = 0
dfs(a, b, M, 0)

print(result)