import heapq

def solution(jobs):
    heap = []
    start, time, now, i = -1, 0, 0, 0
    
    while i < len(jobs):
        for j in jobs:
            if start < j[0] <= now:
                heapq.heappush(heap, [j[1], j[0]])
        if heap:
            disk_1, disk_2 = heapq.heappop(heap)
            start = now
            now += disk_1
            time += (now-disk_2)
            i += 1
        else:
            now += 1
    
    return time//len(jobs)