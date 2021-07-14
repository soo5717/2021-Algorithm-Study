from collections import defaultdict
from itertools import combinations

def solution(relation):
    len_relation = len(relation)
    columns = [i for i in range(len(relation[0]))]
    
    uniqueness = defaultdict(set)
    for len_candidate in range(1, len(relation[0])):
        candidates = list(combinations(columns, len_candidate))
        for candidate in candidates:
            candidate_set = set()
            for row in range(len_relation):
                temp = tuple()
                for col in candidate:
                    temp += (relation[row][col], )
                candidate_set.add(temp)
            if len(candidate_set) == len_relation:
                uniqueness[len_candidate].add(candidate)

    minimality = set()
    for key in uniqueness:
        for value in uniqueness[key]:
            flag_1 = False
            for m in minimality:
                flag_2 = True
                for _m in m:
                    if _m not in value:
                        flag_2 = False
                if flag_2:
                    flag_1 = True
            if not flag_1:
                minimality.add(value)
    return len(minimality)  if len(minimality) else 1