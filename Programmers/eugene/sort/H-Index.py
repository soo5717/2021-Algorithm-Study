def solution(citations):
    len_ci = len(citations)
    citations.sort(reverse=True)
    
    #여러 케이스 고려를 해야한다.
    #1. 배열의 길이보다 큰 수의 논문들만 있다면(=베열의 최소값이 배열의 개수보다 크다면), 그 논문의 개수가 최대 h이다.
    if(citations[-1] >= len_ci):
        return len_ci

    for h in range(citations[0],0,-1): 
        if(h <= len_ci and h <= citations[h-1]): #h번 이상 인용된 논문이 h개 이상이다.
            #나머지 논문에 대한 추가 검증 필요 없음
            return h
    return 0