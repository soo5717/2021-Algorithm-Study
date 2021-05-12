def solution(distance, rocks, n):
    answer = 0
    
    rocks.sort()
    rocks.append(distance)
    
    left, right = 0, distance
    
    while left <= right:
        mid = (left+right) // 2
        min_distance = distance
        del_rock = now = 0
        
        for rock in rocks:
            dis = rock - now
            if dis < mid:
                del_rock += 1
            else:
                now = rock
                min_distance = min(min_distance, dis)
        
        if del_rock > n:
            right = mid-1
        else:
            answer = min_distance
            left = mid+1
            
    return answer