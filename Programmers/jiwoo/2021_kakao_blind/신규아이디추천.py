def solution(new_id):
    #1
    new_id = new_id.lower()
    #2
    answer = ''
    for id_char in new_id:
        if id_char.isalnum() or id_char in '-_.':
            answer += id_char
    #3
    while '..' in answer:
        answer = answer.replace('..', '.')
    #4
    if answer[0] == '.' and len(answer) > 1:
        answer = answer[1:]    
    if answer[-1] == '.':
        answer = answer[:-1]
    #5
    if not answer:
        answer = 'a'
    #6
    answer = answer[:15]
    if answer[-1] == '.':
        answer = answer[:-1]
    #7
    if len(answer) <= 2:
        answer += answer[-1]*(3-len(answer))
    return answer