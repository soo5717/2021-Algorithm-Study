import string

def convert(num, base):
    tmp = string.digits + string.ascii_uppercase
    q, r = divmod(num, base)
    if q == 0:
        return tmp[r]
    else:
        return convert(q, base) + tmp[r]
    
def solution(n, t, m, p):
    
    answer, numbers = '', ''
    max_cnt = t * m
    
    cnt = 0
    while cnt < max_cnt:
        numbers += convert(cnt, n)
        cnt += 1

    
    return numbers[p-1::m][:t]
