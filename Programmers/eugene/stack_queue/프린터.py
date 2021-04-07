from collections import deque

def solution(priorities, location):
    answer = 0
    
    queue=deque(priorities)
    while(queue):
        if location == 0 : #location이 맨 앞으로 왔을 경우
            if queue[0] < max(queue): #더 큰 중요도가 뒤에 있으면
                queue.append(queue.popleft())
                location = len(queue)-1
            else : #loca에 있는 문서의 중요도가 가장 높으면 출력하고 순서 리턴
                return answer+1

        else : #아직 loca차례가 오지 않았을 때
            location -=1
            if queue[0] < max(queue):
                queue.append(queue.popleft())
                
            else :
                queue.popleft()
                answer+=1    
    return answer
