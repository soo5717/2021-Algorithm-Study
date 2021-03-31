def solution(prices):
    len_p=len(prices)
    answer = [(len_p-1)-i for i in range(len_p)]
    
    stack = []
    for i, price in enumerate(prices):
        while stack and prices[stack[-1]] > price:
            j = stack.pop()
            answer[j] = i - j
        stack.append(i)
        
    return answer
