def tenToN(num, n):
    nums = "0123456789ABCDEF"
    
    a = num // n
    b = num % n
    
    if a == 0:
        return nums[b]
    else:
        return tenToN(a, n) + nums[b]

def solution(n, t, m, p):
    answer = ''
    
    num = 0
    while len(answer) < m*t:
        answer += tenToN(num, n)
        num += 1
    return answer[p-1::m][:t]