from heapq import heapify, heappop, heappush

def solution(operations):
    min_heap, max_heap = [], []
    
    for op in operations:    
        if op == "D 1": #최댓값 삭제
            if not max_heap: continue
            max_num = heappop(max_heap)[1]
            min_heap.remove(max_num)
        elif op == "D -1": #최솟값 삭제
            if not min_heap: continue
            min_num = heappop(min_heap)
            max_heap.remove((-min_num, min_num))
        else:
            num = int(op[2:])
            heappush(min_heap, num)
            heappush(max_heap, (-num, num))
    
    return [max_heap[0][1], min_heap[0]] if max_heap and min_heap else [0, 0]