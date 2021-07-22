def solution(str1, str2):
    str1=str1.lower()
    str2=str2.lower()
    
    #두 글짜씩 끊어서 다중집합 생성
    MultiSetX,MultiSetY=[],[]
    for i in range(len(str1)-1):
        if str(str1[i:i+2]).isalpha(): MultiSetX.append(str(str1[i:i+2]))
    for i in range(len(str2)-1): 
        if str(str2[i:i+2]).isalpha(): MultiSetY.append(str(str2[i:i+2]))
            
    #다중집합 교집합, 합집합
    temp_u, temp_i=MultiSetX.copy(),MultiSetX.copy()
    union_XY = MultiSetX.copy()
    intersection_XY=[]
    
    for i in MultiSetY:
        union_XY.append(i) if i not in temp_u else temp_u.remove(i)    
        if i in temp_i:
            temp_i.remove(i) 
            intersection_XY.append(i)
            
    len_uni=len(union_XY)
    len_inter=len(intersection_XY)
    answer = len_inter/len_uni if len_uni else 1
    
    return int(answer*65536)
