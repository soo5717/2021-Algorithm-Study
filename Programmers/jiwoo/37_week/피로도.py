from itertools import permutations

def solution(k, dungeons):
    dungeons_count = len(dungeons)
    answer = 0
    
    for cases in permutations(dungeons, dungeons_count):
        now = k
        count = 0
        for min_tired, use_tired in cases:
            if now >= min_tired:
                now -= use_tired
                count += 1
        if count > answer:
            answer = count
    
    return answer