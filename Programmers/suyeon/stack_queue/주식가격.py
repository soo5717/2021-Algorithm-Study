# prices = {1, 2, 3, 2, 3, 1} return {5, 4, 1, 2, 1, 0}
def solution(prices):
    length = len(prices)
    answer = [ i for i in range (length - 1, -1, -1)]
    
    stack = [0]
    for i in range (1, length, 1):
        # print(i, stack)
        while stack and prices[stack[-1]] > prices[i]:
            j = stack.pop()
            answer[j] = i - j
            # print(i, j, stack)
        stack.append(i)
    return answer