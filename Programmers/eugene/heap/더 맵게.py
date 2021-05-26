import heapq

def solution(scoville, K):
    heapq.heapify(scoville)

    i=0
    while(True):
        if scoville[0] >= K:
            return i
        
        x=heapq.heappop(scoville)
        y=heapq.heappop(scoville)
        heapq.heappush(scoville, x+y*2)
        i+=1
        
        if (len(scoville)==1):
            if scoville[0]<K: return -1
            else : return i
