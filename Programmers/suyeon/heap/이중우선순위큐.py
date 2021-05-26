from heapq import heapify, heappop, heappush

def solution(operations):
    heap = []
    for op in operations:
        if op == "D 1": #최댓값 삭제 
            if not heap: continue
            heap.remove(max(heap))
            heapify(heap)
        elif op == "D -1": #최솟값 삭제
            if not heap: continue
            heappop(heap)
        else:
            _, num = op.split()
            heappush(heap, int(num))
    
    return [max(heap), heap[0]] if heap else [0, 0]