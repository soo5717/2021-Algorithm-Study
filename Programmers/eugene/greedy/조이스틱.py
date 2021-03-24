def solution(name):
    answer,i = 0,0
    name=list(name)
    len_name = len(name)
    
    while(True):
        left, right =1,1
        
        #알파벳 카운트 : A가 아니면 알파벳 변경을 시도
        if name[i] != 'A': 
            answer+=min(ord(name[i]) - ord('A'), ord('Z')-ord(name[i])+1)
            
        #변경한 위치는 A로 변경하고, 모든 문자열이 A로 바뀌면 종료.
        name[i] = 'A'
        if ['A'] * len_name == name:
            break
            
        #커서 이동 카운트
        for k in range(1,len_name):
            if name[i+k]=="A": right+=1
            else : break 
            
            if name[i-k]=="A" : left+=1               
            else: break
        
        #left/right 중 더 가까운 방향으로 이동            
        answer += left if left < right else right
        i += -left if left < right else right
    return answer
