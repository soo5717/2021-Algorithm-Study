def cycle(x, y, d, grid):
    cnt = 0 
    end = (x, y, d)
    visited[x][y][d] = True
    
    dx = [0, 1, 0, -1]
    dy = [1, 0, -1, 0]
    nx, ny, nd = x, y, d
    while True:
        # 좌표 갱신 nx, ny
        nx = (nx+dx[nd]) % len(grid)
        ny = (ny+dy[nd]) % len(grid[0])
        
        cnt += 1
        if grid[nx][ny] == 'R':
            nd = (nd+1)%4
        elif grid[nx][ny] == 'L':
            nd = (nd-1)%4
        
        #종료조건 : 최초의 시작점과 방향이 모두 일치하면
        if visited[nx][ny][nd]:
            if x == nx and y == ny and d == nd:
                return cnt
            else:
                return 0
        #사이클이 생기지 않는 걸 확신할 수 있는 조건을 모르겠다.
        visited[nx][ny][nd] = True
            
def solution(grid):
    global visited 
    answer = []
    visited = [[[False]*4 for _ in range(len(grid[0]))] for _ in range(len(grid))]
    
    for row in range(len(grid)):
        for col in range(len(grid[0])):
            for d in range(4): #direction
                if not visited[row][col][d]:
                    dist = cycle(row, col, d, grid)
                    if dist:
                        answer.append(dist)
    answer.sort()
    return answer
