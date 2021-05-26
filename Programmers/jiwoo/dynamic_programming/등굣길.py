def solution(m, n, puddles):
    memo = [[0]*(n+1) for i in range(m+1)]
    
    if puddles:
        for a, b in puddles:
            memo[a][b] = -1
            
    memo[1][1] = 1
    
    for j in range(1, m+1):
        for k in range(1, n+1):
            if j == k == 1:
                continue
            if memo[j][k] == -1:
                memo[j][k] = 0
                continue
            memo[j][k] = (memo[j][k-1] + memo[j-1][k])  % 1000000007

    return memo[m][n]