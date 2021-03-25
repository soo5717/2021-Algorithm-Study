from itertools import permutations

def solution(numbers):
    numberAll = []
    for i in range(1, len(numbers)+1):
        a = list(permutations(numbers, i))
        for j in range(len(a)):
            b = int(''.join(map(str, a[j])))
            if isPrime(b):
                numberAll.append(b)
    numberAll = list(set(numberAll))          
    return len(numberAll)

def isPrime(n):
    if n == 0 or n == 1:
        return False
    else:
        for i in range(2, n):
            if n % i == 0:
                return False
        return True