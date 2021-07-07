def separate(p): # 문자열 u, v로 분리
    u, v = '', ''
    count = 0
    for i, pp in enumerate(p):
        count += 1 if pp == '(' else -1
        if count == 0: 
            u, v = p[:i+1], p[i+1:]
            break
    return u, v 

def is_correct(p): # 올바른 괄호 문자열인지 판단
    stack = []
    for pp in p:
        if pp == '(': 
            stack.append('(')
        elif stack: 
            stack.pop()
    return True if not stack else False

def convert(p): 
    if not p: return p # 1단계
    u, v = separate(p) # 2단계

    if is_correct(u): # 3단계
        return u + convert(v)
    else: # 4단계
        u = ''.join([')' if uu == '(' else '(' for uu in u[1:-1]])
        return '(' + convert(v) + ')' + u
        
def solution(p):
    return p if is_correct(p) else convert(p)