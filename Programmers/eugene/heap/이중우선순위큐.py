import heapq
def solution(operations):
    
    I_cnt, D_cnt = 0,0
    min_heap, max_heap=[],[]
    
    for oper in operations:
        if(oper[0]=="I"):
            I_cnt+=1
            num=int(oper[2:])
            heapq.heappush(min_heap, num)
            heapq.heappush(max_heap, (-num, num))
        else :
            D_cnt+=1
            if(D_cnt >= I_cnt):
                min_heap, max_heap=[],[]
                I_cnt, D_cnt = 0,0
                continue
            
            if(oper =="D 1") :
                heapq.heappop(max_heap) 
            else :
                heapq.heappop(min_heap) 
            
    if (D_cnt == I_cnt):
        print(min_heap, max_heap)
        return [0,0]
    else:
        return [max_heap[0][1], min_heap[0]]
