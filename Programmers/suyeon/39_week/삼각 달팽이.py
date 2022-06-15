# 아래, 오른쪽, 위
dx = [1, 0, -1]
dy = [0, 1, -1]

def solution(n):
    matrix = [[0] * i for i in range(1, n + 1)]
    
    x, y = -1, 0
    num, idx = 0, -1
    
    for count in range(n, 0, -1):
        idx = (idx + 1) % 3
        for _ in range(count):
            num += 1
            x += dx[idx]
            y += dy[idx]
            matrix[x][y] = num 
        
    return [col for row in matrix for col in row]