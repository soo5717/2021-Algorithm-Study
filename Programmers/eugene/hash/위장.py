def solution(clothes):
    answer = 1

    clothes= dict(clothes)
    category = set(clothes.values())
    Clothes = dict(zip(category, [0]*len(category)))
    
    for c in clothes.values():
        Clothes[c]+=1    
    
    for value in Clothes.values():
        answer*= (value+1)        
    answer-=1    

    return answer