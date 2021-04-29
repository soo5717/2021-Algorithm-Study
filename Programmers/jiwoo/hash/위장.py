def solution(clothes):
    answer = {}
    
    for i in clothes:
        if i[1] in answer:
            answer[i[1]] += 1
        else:
            answer[i[1]] = 2
    
    count = 1
    for i in answer.values():
        count *= i
    
    return count-1