def solution(distance, rocks, n):
    rocks.sort()
    rocks.append(distance)
    
    answer = 0
    start, end = 1, distance # answer은 1 ~ distance 사이에 있음
    while start <= end:
        mid = (start + end) // 2
        
        # 부서진 바위의 수 세기
        cnt_rock, prev_rock = 0, 0
        for rock in rocks:
            if rock - prev_rock < mid:
                cnt_rock += 1
            else:
                prev_rock = rock
            
        if cnt_rock > n: # 더 많이 파괴되었을 경우
            end = mid - 1
        else: # 같거나 더 작게 파괴되었을 경우
            answer = mid
            start = mid + 1
            
    return answer