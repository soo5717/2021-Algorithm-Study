from collections import deque

# 시계 방향 (좌, 하, 우, 상)
dx = [0, 1, 0, -1]
dy = [-1, 0, 1, 0]

def get_cycle_length(grid, visited, x, y, d):
    row, col = len(grid), len(grid[0])
    
    count = 0
    
    while not visited[x][y][d]:    
        count += 1
        visited[x][y][d] = True
        
        if(grid[x][y] == 'L'):
            d = (d + 1) % 4
        elif(grid[x][y] == 'R'):
            d = (d - 1) % 4
        
        x = (x + dx[d]) % row
        y = (y + dy[d]) % col
    
    return count

def solution(grid):
    row, col = len(grid), len(grid[0])
    
    answer = []
    visited = [[[False] * 4 for _ in range(col)] for _ in range(row)]
    
    for x in range(row):
        for y in range(col):
            for d in range(4):
                if not visited[x][y][d]:
                    answer.append(get_cycle_length(grid, visited, x, y, d))
        
    return sorted(answer)