import heapq

def solution(jobs):
    heap = []
    start, time, now, i = -1, 0, 0, 0
    
    while i < len(jobs):
        for j in jobs:
            if start < j[0] <= now:
                heapq.heappush(heap, [j[1], j[0]])
        if len(heap) > 0:
            disk = heapq.heappop(heap)
            start = now
            now += disk[0]
            time += (now-disk[1])
            i += 1
        else:
            now += 1
    
    return int(time/len(jobs))