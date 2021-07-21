from collections import defaultdict

def solution(N, stages):
    stage_dict = defaultdict(int)
    for stage in stages:
        stage_dict[stage] += 1
        
    result = {}
    users = len(stages)
    for i in range(1, N+1):
        users -= stage_dict[i-1]
        result[i] = stage_dict[i]/users if users else 0
    return sorted(result, key=lambda x: result[x], reverse = True)