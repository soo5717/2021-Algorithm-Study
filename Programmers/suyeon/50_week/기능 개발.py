
from collections import deque

def solution(progresses, speeds):
    progresses = deque(progresses)
    speeds = deque(speeds)
    
    answer = []
    
    while progresses:
        for idx, speed in enumerate(speeds):
            progresses[idx] += speed
        
        count = 0
        
        while progresses and progresses[0] >= 100:
            progresses.popleft()
            speeds.popleft()
            count += 1
        
        if count:
            answer.append(count)
    
    return answer