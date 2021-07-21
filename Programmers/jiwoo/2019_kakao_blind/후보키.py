from itertools import combinations

def solution(relations):
    row = len(relations)
    col = len(relations[0])
    
    candidates = [[] for i in range(col+1)]

    min_key = []
    for i in range(1, col+1):
        candidates[i] = combinations(range(col), i)
        for candidate in candidates[i]:
            not_key = 0
            unique = [[] for _ in range(row)]
            # 유효성 검사
            for k in candidate:
                for r_ in range(row):
                    unique[r_].append(relations[r_][k])
            for i in unique:
                if unique.count(i) >= 2:
                    not_key = 1
                    break
            # 최소성 검사
            if not_key == 0:
                if len(candidate) == 1:
                    min_key.append(candidate)
                else :
                    for r_ in min_key:
                        if set(r_).issubset(set(candidate)):
                            break
                    else:
                        min_key.append(candidate)
    return len(min_key)