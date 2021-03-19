def solution(name):
    answer = 0
    
    name=list(name)
    i=0
    
    while(True):
        left=1
        right=1

        #알파벳 카운트 : A가 아니면 알파벳 변경을 시도
        if name[i] != 'A': 
            if( ord(name[i]) - ord('A') < 13) :
                answer+=ord(name[i]) - ord('A')
            else :
                answer+=ord('Z')-ord(name[i])+1
        #변경한 위치는 A로 바꾼다.
        name[i] = 'A'
                  
        #종료 조건 : 모든 위치가 A로 바뀌면 종료한다. 
        if ['A'] * len(name) == name:
            break
            
        #커서 이동 카운트
        for k in range(1,len(name)):
            if name[i+k]=="A": 
                right+=1
            else: 
                break
                
        for k in range(1,len(name)):
            if name[i-k]=="A": 
                left+=1               
            else: 
                break
        
        #left/right 중 더 가까운 방향으로 이동        
        if left<right:
            answer+=left
            i-=left
        else:
            answer+=right
            i+=right
    return answer
