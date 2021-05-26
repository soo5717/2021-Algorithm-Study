def solution(triangle):
    for i in range (1,len(triangle)): #전체
        for j in range(i+1): #한 줄씩
            if (j==0): #줄의 맨 처음
                triangle[i][j] += triangle[i-1][0]
            elif j==i : #줄의 맨 끝
                triangle[i][j] += triangle[i-1][-1]
            else : #중간
                triangle[i][j] += max(triangle[i - 1][j - 1], triangle[i - 1][j])
    #전체 다 돌고, 마지막 temp에서 가장 큰 값 리턴
    return max(triangle[-1])
