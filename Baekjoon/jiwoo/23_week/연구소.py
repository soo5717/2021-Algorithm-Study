import sys
input = sys.stdin.readline

N, M = map(int, input().split())
virus_map = [list(map(int, input().split())) for _ in range(N)]
temp = [[0] * M for _ in range(N)]

dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

result = 0
def virus(x, y):
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]

        if 0 <= nx and nx < N and 0 <= ny and ny < M:
            if temp[nx][ny] == 0:
                temp[nx][ny] = 2
                virus(nx, ny)
            
def safe():
    count = 0
    for i in range(N):
        for j in range(M):
           if temp[i][j] == 0:
            count += 1
    return count

def dfs(count):
    global result
    if count == 3:
        for i in range(N):
            for j in range(M):
                temp[i][j] = virus_map[i][j]
        for i in range(N):
            for j in range(M):
                if temp[i][j] == 2:
                    virus(i, j)
        result = max(result, safe())
        return 
    for i in range(N):
        for j in range(M):
            if virus_map[i][j] == 0:
                virus_map[i][j] = 1
                count += 1
                dfs(count)
                virus_map[i][j] = 0
                count -= 1

dfs(0)
print(result)