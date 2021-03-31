def solution(priorities, location):
    answer = 0
    
    while(priorities):
        if location == 0 : #location이 맨 앞으로 왔을 경우
            if priorities[0] < max(priorities): #더 큰 중요도가 뒤에 있으면
                priorities.append(priorities.pop(0))
                location = len(priorities)-1
            else : #loca에 있는 문서의 중요도가 가장 높으면 출력하고 순서 리턴
                return answer+1
            
            
        else : #아직 loca차례가 오지 않았을 때
            location -=1
            if priorities[0] < max(priorities):
                priorities.append(priorities.pop(0))
                
            else :
                priorities.pop(0) #
                answer+=1    
    return answer
