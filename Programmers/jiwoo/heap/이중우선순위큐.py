import heapq

def solution(operations):
    heap = []
    max_heap = []
    
    for o in operations:
        operation = o.split()
        if operation[0] == "I":
            num = int(operation[1])
            heapq.heappush(heap, num)
            heapq.heappush(max_heap, (num*-1, num))
        else:
            if len(heap) == 0:
                pass
            elif operation[1] == '1':
                max_num = heapq.heappop(max_heap)[1]
                heap.remove(max_num)
            elif operation[1] == '-1':
                min_num = heapq.heappop(heap)
                max_heap.remove((min_num*(-1), min_num))
                
    if heap:
        return [heapq.heappop(max_heap)[1], heapq.heappop(heap)]
    else:
        return [0, 0]