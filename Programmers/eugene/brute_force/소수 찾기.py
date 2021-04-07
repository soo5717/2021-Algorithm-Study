from itertools import permutations

def prime_tf(number): #소수 판별
    return all([(number%n) for n in range(2, int(number**0.5)+1)]) and number>1

def solution(numbers):
    answer = 0
    numbers=list(numbers)
    prime_list=[]
    
    for i in range(1, len(numbers)+1):
        prime_list += list(map(int, map(''.join,permutations(numbers, i)))) #모든 조합을 prime_list에 추가
    prime_list=set(prime_list) #중복 제외
    
    for j in prime_list :
        if prime_tf(j) : #True
            answer+=1
    return answer
