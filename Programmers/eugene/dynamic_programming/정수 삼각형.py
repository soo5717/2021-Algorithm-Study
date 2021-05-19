def solution(triangle):
    answers=[triangle[0]]
    for i, tr in enumerate(triangle): #전체
        if i==0: continue
        temp=[]
        for j, value in enumerate(tr): #한 줄씩
            #맨 처음과 끝은 바로 위 answers[i-1][0], answers[i-1][i]를 value에 더해준다.
            #나머지 위치들은 양옆을 비교해서 큰 값을 더해준다.
            if (j==0): #줄의 맨 처음
                temp.append(answers[i-1][0]+value)
            elif j==i : #줄의 맨 끝
                temp.append(answers[i-1][i-1]+value)
            else : #중간
                temp.append(max(answers[i-1][j-1], answers[i-1][j])+value)
        answers.append(temp)
    #전체 다 돌고, 마지막 temp에서 가장 큰 값 리턴
    return max(temp)
