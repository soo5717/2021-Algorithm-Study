def solution(citations):
    len_ci = len(citations)
    citations.sort(reverse=True)

    for h in range(citations[0],-1,-1): 
        if(h <= len_ci and h <= citations[h-1]): #h번 이상 인용된 논문이 h개 이상이다.
            return h
    return 0