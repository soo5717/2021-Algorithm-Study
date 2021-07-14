def solution(record):
    nickname_dict = {}
    
    for rec in record:
        rec = rec.split()
        if rec[0] == 'Enter' or rec[0] == 'Change': 
            nickname_dict[rec[1]] = rec[2]

    answer = []
    for rec in record:
        rec = rec.split()
        nickname = nickname_dict[rec[1]]
        if rec[0] == 'Enter':
            answer.append(nickname + '님이 들어왔습니다.')
        elif rec[0] == 'Leave':
            answer.append(nickname + '님이 나갔습니다.') 
    return answer