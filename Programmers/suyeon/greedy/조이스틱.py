def solution(name):
    # 상하 이동
    up_down = [min(ord(n) - ord('A'), ord('Z') - ord(n) + 1) for n in name]
    
    idx, answer = 0, 0
    # 좌우 이동
    while True:
        answer += up_down[idx]
        up_down[idx] = 0
        if sum(up_down) == 0:
            return answer
        
        left, right = 1, 1
        while up_down[idx - left] == 0:
            left += 1
        while up_down[idx + right] == 0:
            right += 1  
        answer += left if left < right else right
        idx += -left if left < right else right