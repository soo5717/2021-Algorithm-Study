from itertools import permutations

def solution(k, dungeons): 
    answer = -1

    for perm_dungeons in permutations(dungeons, len(dungeons)):
        count, min_k = 0, k
        for min_hp, hp in perm_dungeons:
            if min_k >= min_hp:
                count += 1
                min_k -= hp

        if count > answer:
            answer = count 

    return answer