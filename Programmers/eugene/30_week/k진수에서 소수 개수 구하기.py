import math 

def solution(n, k):
    answer = 0

    numbers = change(n, k)
    temp = ''
    
    kkk = numbers.split('0')

    for k in kkk:
        if k != '' and isPrime(int(k)):
            answer += 1
    return answer

def isPrime(x):
    if x == 2:
        return True
    
    if x == 1 or x % 2 == 0:
        return False
    
    for i in range(3, int(math.sqrt(x))+1, 2):
        if x % i == 0 :
            return False
    return True

def change(n, q):
    rev_base = ''

    while n > 0:
        n, mod = divmod(n, q)
        rev_base += str(mod)

    return rev_base[::-1]
