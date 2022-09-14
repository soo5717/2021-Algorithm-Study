ooz = '110'


def split_ooz(x):
    count, stack = 0, []
    
    for token in x:
        if token != '0' or stack[-2:] != ['1', '1']:
            stack.append(token)
            continue
        
        stack.pop()
        stack.pop()
        count += 1
    
    return (count, ''.join(stack))

        
def get_min_order(x):
    count, x = split_ooz(x)
    
    idx_oo = x.find('11')
    
    if idx_oo != -1:
        return x[:idx_oo] + ooz * count + x[idx_oo:]
    
    idx_last_z = x.rfind('0')
    
    if idx_last_z != -1:
        return x[:idx_last_z + 1] + ooz * count + x[idx_last_z + 1:]
    
    return ooz * count + x


def solution(s):
    return [get_min_order(x) for x in s]