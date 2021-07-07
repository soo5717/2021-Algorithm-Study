def slicing_uv(p):
    open_count = 0
    close_count = 0
    for i in range(len(p)):
        if p[i] == '(':
            open_count += 1
        else:
            close_count += 1
        if open_count == close_count:
            return p[:i+1], p[i+1:]

def isOk(u):
    stack = []
    for u_ in u:
        if u_ == '(':
            stack.append(u_)
        else:
            if not stack:
                return False
            stack.pop()
    return True

def solution(p):
    answer = ''
    if not p:
        return ''
    
    u, v = slicing_uv(p)
    
    if isOk(u):
        return u + solution(v)
    else:
        answer += '('
        answer += solution(v)
        answer += ')'
        for u_ in u[1:-1]:
            if u_ == '(':
                answer += ')'
            else:
                answer += '('
    return answer