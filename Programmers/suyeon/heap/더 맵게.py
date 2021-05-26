import heapq

def solution(scoville, K):
    heapq.heapify(scoville)
    
    answer = 0
    while True:  
        first = heapq.heappop(scoville)
        if not scoville:
            return -1 if first < K else answer
        elif first < K:
            second = heapq.heappop(scoville)
            heapq.heappush(scoville, first + second * 2)
            answer += 1
        else:
            return answer