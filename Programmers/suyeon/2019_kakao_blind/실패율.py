from collections import defaultdict

def solution(N, stages):
    stage_dict = defaultdict(int)
    for stage in stages:
        stage_dict[stage] += 1
    
    answer = {}
    user = len(stages)
    for i in range(1, N + 1):
        user -= stage_dict[i - 1]
        answer[i] = stage_dict[i]/user if user else 0
    
    return sorted(answer, key=lambda x: answer[x], reverse=True)