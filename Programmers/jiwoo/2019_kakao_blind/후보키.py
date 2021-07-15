from itertools import combinations

def solution(relations):
    row = len(relations)
    col = len(relations[0])
    
    candidates = [[] for i in range(col+1)]
    for i in range(col+1):
        candidates[i] = combinations(range(col), i)

    min_key = []
    for i in range(1, col+1):
        for j in candidates[i]:
            not_key = 0
            s = [[] for _ in range(row)]
            for k in j:
                for r in range(row):
                    s[r].append(relations[r][k])
            for i in s:
                if s.count(i) >= 2:
                    not_key = 1
                    break
            if not_key == 0:
                if len(j) == 1:
                    min_key.append(j)
                else :
                    for r in min_key:
                        if set(r).issubset(set(j)):
                            break
                    else:
                        min_key.append(j)
    return len(min_key)