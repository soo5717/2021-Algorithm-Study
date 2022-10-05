from itertools import combinations_with_replacement

def solution(n, apeach_info):
    answer = []
    diff = 0
    
    for case in combinations_with_replacement(range(11), n):
        lion_info = [0] * 11
        
        for i in case:
            lion_info[10 - i] += 1
            
        apeach_score, lion_score = 0, 0
        
        for i, (apeach, lion) in enumerate(zip(apeach_info, lion_info)):
            if not apeach and not lion:
                continue
                
            if apeach >= lion:
                apeach_score += 10 - i
            else:
                lion_score += 10 - i
            
        if lion_score - apeach_score > diff:
            diff = lion_score - apeach_score
            answer = lion_info
            
    return answer or [-1]