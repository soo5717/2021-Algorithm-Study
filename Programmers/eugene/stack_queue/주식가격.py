def solution(prices):
    len_p=len(prices)
    answer = [ i for i in range (len_p - 1, -1, -1)]
    
    stack = [0]
    for i in range(1, len_p):
        while stack and prices[i] < prices[stack[-1]]:
            j = stack.pop()
            answer[j] = i - j
        stack.append(i)
        
    return answer
