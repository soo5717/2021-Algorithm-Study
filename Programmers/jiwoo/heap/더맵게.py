import heapq

def solution(scoville, K):
    count = 0
    
    heapq.heapify(scoville)
    
    while scoville[0] < K:
        try:
            count += 1
            heapq.heappush(scoville, heapq.heappop(scoville) + heapq.heappop(scoville)*2)
        except IndexError:
            return -1
    return count