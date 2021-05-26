def solution(triangle):
    for i in range(1, len(triangle)):
        for j in range(i+1):
            if j == 0:
                triangle[i][j] += triangle[i-1][0]
            elif j == i:
                triangle[i][j] += triangle[i-1][-1]
            else:
                a = triangle[i][j] + triangle[i-1][j-1]
                b = triangle[i][j] + triangle[i-1][j]
                triangle[i][j] = max(a, b)
    
    return max(triangle[i])