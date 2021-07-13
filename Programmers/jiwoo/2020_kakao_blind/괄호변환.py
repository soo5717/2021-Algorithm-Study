def slice_check(p):
    count = 0
    isOK = True
    for i in range(len(p)):
        if p[i] == '(':
            count += 1
        else:
            count -= 1
        if count < 0:
            isOK = False
        if not count:
            return p[:i+1], p[i+1:], isOK

def solution(p):
    answer = ''
    if not p: return ''
    
    u, v, isOK = slice_check(p)
    
    if isOK:
        return u + solution(v)
    else:
        reverse = ''.join([')' if  u_ == '(' else '(' for u_ in u[1:-1]])
        answer += '(' + solution(v) + ')' + reverse
    return answer