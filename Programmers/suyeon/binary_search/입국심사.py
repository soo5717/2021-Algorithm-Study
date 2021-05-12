def solution(n, times):
    times.sort()
    
    answer = 0
    start, end = 1, times[0] * n
    while start <= end:
        mid = (start + end) //2
        
        # 심사 가능한 최대 인원
        cnt = 0
        for time in times:
            cnt += mid // time 
        
        if cnt < n:
            start = mid + 1
        else:
            answer = mid
            end = mid - 1 
    
    return answer