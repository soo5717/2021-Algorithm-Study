from collections import deque

def solution(priorities, location):
    queue = deque(priorities)

    answer = 0
    while location >= 0:
        left = queue.popleft()
        location -= 1
    
        if any(q > left for q in queue):
            queue.append(left)
            if location == -1:
                location = len(queue) -1
        else:
            answer += 1
    return answer