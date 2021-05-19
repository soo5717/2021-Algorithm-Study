def solution(m, n, puddles):
    DP = [[0] * (m + 1) for _ in range(n + 1)] 
    for x, y in puddles: DP[y][x] = -1
        
    DP[1][1] = 1
    for i in range(1, n + 1):
        for j in range(1, m + 1):
            if i == 1 and j == 1:
                continue
            elif DP[i][j] == -1:
                DP[i][j] = 0
            else:
                DP[i][j] = (DP[i - 1][j] + DP[i][j - 1]) % 1000000007
    return DP[-1][-1]