from math import sqrt

def is_prime(n):
    if n == 2:
        return True
    
    if n % 2 == 0 or n == 1:
        return False
    
    for i in range(3, int(sqrt(n)) + 1, 2):
        if n % i == 0:
            return False
    
    return True


def convert(q, k):
    temp = ''
    
    while True:
        q, r = divmod(q, k)
        temp = str(r) + temp
        
        if q <= 1:
            temp = str(q) + temp
            break
            
    return temp 


def solution(n, k):
    answer = 0 
    
    for num in convert(n, k).split('0'):
        if num != '' and is_prime(int(num)):
            answer += 1
    
    return answer