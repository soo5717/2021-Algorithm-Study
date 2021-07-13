def solution(record):
    answer = []
    names={}
    for r in record:
        temp=r.split()
        #user_id에 따른 이름 설정
        if temp[0]=='Enter' or temp[0] =='Change': 
            names[temp[1]]=temp[2]
            
    for r in record:
        temp=r.split()
        if temp[0]=='Enter':
            answer+=[names[temp[1]]+"님이 들어왔습니다."]
        elif temp[0] =='Leave':
            answer+=[names[temp[1]]+"님이 나갔습니다."]
    return answer
