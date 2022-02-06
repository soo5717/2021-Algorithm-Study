HEX_DICT = { 10 : 'A', 11 : 'B', 12 : 'C', 13 : 'D', 14 : 'E', 15 : 'F' }

def convert(number, n):
    if number <= 1:
        return '1' if number == 1 else ''
    
    q, r = divmod(number, n)
    temp = HEX_DICT[r] if r in HEX_DICT else str(r) 
    
    return convert(q, n) + temp
    
def solution(n, t, m, p):
    answer = ''
    number = 0
    
    while len(answer) < t * m:
        temp = convert(number, n)
        if temp == '':
            temp = '0'
        answer += temp
        number += 1
    
    return answer[p - 1::m][:t]