from collections import deque
from heapq import heapify, heappop, heappush

def solution(jobs):
    queue = deque(sorted(jobs))
    
    heap = []
    answer, count, now = 0, 0, 0
    while count < len(jobs):
        while queue and queue[0][0] <= now:
            call, time = queue.popleft()
            heappush(heap, (time, call))
            
        if not heap:
            now = queue[0][0]
        else:
            time, call = heappop(heap)
            answer += time + (now - call)
            now += time
            count += 1
    return answer // count