def solution(n, times):
    answer = 0
    
    left = 1
    right = min(times) * n
    
    while left <= right:
        mid = (left+right) // 2
        remain = n
        for time in times:
            remain -= mid // time
            if remain <= 0:
                answer = mid
                right = mid - 1
                break
        if remain > 0:
            left = mid + 1
        
    return answer