def solution(p):
    if not p: return p
    
    count = 0
    is_correct = True
    for i, pp in enumerate(p):
        count += 1 if pp == '(' else -1
        
        if count < 0:
            is_correct = False
        elif count == 0: 
            u, v = p[:i+1], p[i+1:]
            
            if is_correct:
                return u + solution(v)
            else:
                u = ''.join([')' if uu == '(' else '(' for uu in u[1:-1]])
                return '(' + solution(v) + ')' + u