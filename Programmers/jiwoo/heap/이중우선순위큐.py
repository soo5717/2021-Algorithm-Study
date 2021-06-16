import heapq

def solution(operations):
    min_heap = []
    max_heap = []
    
    for o in operations:
        operation = o.split()
        if operation[0] == "I":
            num = int(operation[1])
            heapq.heappush(min_heap, num)
            heapq.heappush(max_heap, (-num, num))
        else:
            if not min_heap:
                pass
            elif operation[1] == '1':
                max_num = heapq.heappop(max_heap)[1]
                min_heap.remove(max_num)
            elif operation[1] == '-1':
                min_num = heapq.heappop(min_heap)
                max_heap.remove((-min_num, min_num))
                
    return [heapq.heappop(max_heap)[1], heapq.heappop(min_heap)] if min_heap else [0,0]