def solution(number, k):
    stack = [number[0]]
    for num in number[1:]:

        while len(stack) > 0 and stack[-1] < num and k > 0:
            k -= 1
            stack.pop()

        stack.append(num)

    if k != 0:
        stack = stack[:-k]
    return ''.join(stack)
