def solution(clothes):
    dictionary = dict()
    for cloth in clothes:
        dictionary[cloth[-1]] = dictionary.get(cloth[-1], 0) + 1 
    
    answer = 1
    for value in dictionary.values():
        answer *= value + 1
    return answer - 1