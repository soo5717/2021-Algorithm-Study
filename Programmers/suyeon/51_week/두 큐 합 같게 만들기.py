from collections import deque

def solution(queue1, queue2):
    sum1, sum2 = sum(queue1), sum(queue2)
    queue1, queue2 = deque(queue1), deque(queue2)
    
    answer = 0
    max_count = len(queue1) * 2 + 1
    
    while True:    
        if sum1 == sum2:
            break
            
        if answer > max_count:
            answer = -1
            break
        
        answer += 1
        
        if sum1 > sum2:
            sum1 -= queue1[0]
            sum2 += queue1[0]
            queue2.append(queue1.popleft())
        else:
            sum2 -= queue2[0]
            sum1 += queue2[0]
            queue1.append(queue2.popleft())
            
    return answer