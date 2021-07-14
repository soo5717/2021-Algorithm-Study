def solution(N, stages):
    result = {}
    users = len(stages)
    
    for i in range(1, N+1):
        if users != 0:
            count = stages.count(i)
            result[i] = (count/users)
            users -= count
        else:
            result[i] = 0
    return sorted(result, key=lambda x: result[x], reverse = True)