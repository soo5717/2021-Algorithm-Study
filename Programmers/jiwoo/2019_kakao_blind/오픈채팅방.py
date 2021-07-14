def solution(records):
    result = []
    user_nick = {}
    
    for record in records:
        record_split = record.split(' ')
        command = record_split[0]
        if command == "Enter" or command == "Change":
            user_nick[record_split[1]] = record_split[2]
            
    for record in records:
        record_split = record.split(' ')
        command = record_split[0]
        if command == "Enter":
            comment = user_nick[record_split[1]] + "님이 들어왔습니다."
            result.append(comment)
        elif command == "Leave":
            comment = user_nick[record_split[1]] + "님이 나갔습니다."
            result.append(comment)
    return result