def solution(m, n, puddles):
    location=[[1,1]]
    arr = [[0] * (n+1) for _ in range(m+1)]
    arr[1][1] = 1
    for x in range(1,m+1):
        for y in range(1, n+1):
            if [x,y] in puddles:
                continue
            if [x,y]==[1,1]: #출발점에
                continue
            arr[x][y] = arr[x-1][y] + arr[x][y-1]
    return arr[-1][-1] % 1000000007
