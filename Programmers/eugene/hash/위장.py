def solution(clothes):
    answer = 1

    clothes= dict(clothes)
    category = set(clothes.values())
    dict_clothes = dict(zip(category, [0]*len(category)))
    
    for c in clothes.values():
        dict_clothes[c]+=1    
    
    for value in dict_clothes.values():
        answer*= (value+1)        

    return answer-1