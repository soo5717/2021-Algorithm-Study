# Counter, reduce를 사용한 풀이도 가능
# get 대신 defauldict 사용 가능

def solution(clothes):
    dictionary = dict()
    for name, kind in clothes:
        dictionary[kind] = dictionary.get(kind, 1) + 1 
    
    answer = 1
    for value in dictionary.values():
        answer *= value
    return answer - 1