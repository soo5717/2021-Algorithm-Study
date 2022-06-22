from itertools import permutations

def solution(k, dungeons):
    answer = -1
    len_dungeons = len(dungeons)
    
    for data in permutations(dungeons, len_dungeons):
        hp, cnt = k, 0
        for min_tired, use_tired in data:
            if hp < min_tired:
                continue
            hp -= use_tired
            cnt += 1
        
        answer = answer if answer > cnt else cnt
        if answer == len_dungeons:
            break
    
    return answer
