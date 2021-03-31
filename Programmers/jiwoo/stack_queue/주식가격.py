from collections import deque

def solution(prices):
    answer = []
    
    prices_deq = deque(prices)
    
    while prices_deq:
        price = prices_deq.popleft()
        timeCount = 0
        for i in prices_deq:
            timeCount += 1
            if i < price:
                break
        answer.append(timeCount)
    
    return answer