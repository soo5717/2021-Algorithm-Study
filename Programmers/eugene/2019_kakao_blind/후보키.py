from itertools import combinations

def solution(relation):
    combi=[]
    result=0   
    col_len=len(relation[0])
    col_list=[i for i in range(col_len)]
    for i in range(1,col_len+1):    
        combi+=list(combinations(col_list,i))
        
    while combi:
        temp=list(combi)
        if candidate_check(combi[0],relation):  #0번째 조합이 후보키인지 판별:
            result+=1
            for c in combi:
                if include_check(c,combi[0]):
                    temp.remove(c)
        else: temp.remove(combi[0])
        combi=temp
    return result

def candidate_check(c,relation): #받은 인자 c가 후보키인지 판별
    candi_temp=[[] for _ in range(len(relation))]
    c=list(c)
    for i in c:
        for j in range(len(relation)):
            candi_temp[j]+=[relation[j][i]]
    return False if len(candi_temp) != len(set(list(map(tuple,candi_temp)))) else True 

def include_check(items,item):
    for n in item:
        if n not in items: return False
    return True
