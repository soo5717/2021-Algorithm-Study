from itertools import permutations

# 에라토스테네스의 체
def prime_list(n):
    prime = [True] * (n + 1)
    prime[0] = prime[1] = False 
    
    for i in range(2, int(n ** 0.5) + 1):
        if prime[i]:
            for j in range(i*i, len(prime), i):
                prime[j] = False
    return prime
    
def solution(numbers):
    numbers = list(numbers)
    number_set = set()
    
    # 가능한 모든 경우의 수 (순열) => set 사용해서 중복 제거
    for i in range(len(numbers)):
        number_set |= set(map(int, map(''.join, permutations(numbers, i + 1))))
    
    # 에라토스테네스의 체로 소수 판별 리스트 생성
    prime = prime_list(max(number_set))
    
    # 소수 판별
    answer = 0
    for number in number_set:
        if prime[number]:
            answer += 1
    return answer