from collections import deque

def solution(numbers, target):
    
    queue = deque([0]) #numbers 순서에 따라 매번 변한다.
    for n in numbers :
        sub_q = []
        for i in queue :
            sub_q.append(i+n)
            sub_q.append(i-n)
        queue = sub_q
    return queue.count(target)
