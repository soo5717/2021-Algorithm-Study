from collections import deque

def solution(numbers, target):
    
    queue = deque([0])
    for n in numbers :
        sub_q = []
        for i in queue :
            sub_q.append(i+n)
            sub_q.append(i-n)
        queue = sub_q
    return queue.count(target)
