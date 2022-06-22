def solution(n):
    snail = [[0 for _ in range(i)] for i in range(1, n+1) ]
    
    num, x, y = 0, -1, 0
    dx = [1, 0, -1]
    dy = [0, 1, -1]
    
    for nn in range(n):
        i = nn%3
        for k in range(n-nn):
            num += 1
            x = x+dx[i]
            y = y+dy[i]
            snail[x][y] = num

    return sum(snail, [])
