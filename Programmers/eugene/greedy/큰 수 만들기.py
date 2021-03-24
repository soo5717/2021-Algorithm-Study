def solution(number, k):
    stack = [number[0]]
    for num in number[1:]:

        while stack and stack[-1]<num and k>0:
            k -= 1
            stack.pop()
        stack.append(num)

    return ''.join(stack[:len(stack) - k])
