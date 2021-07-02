def solution(info, query):
    answer = []
    for q in query:
        count = 0
        order = q.split()
        for i in info:
            person = i.split()
            if order[0] != "-":
                if order[0] != person[0]:
                    continue
            if order[2] != "-":
                if order[2] != person[1]:
                    continue
            if order[4] != "-":
                if order[4] != person[2]:
                    continue
            if order[6] != "-":
                if order[6] != person[3]:
                    continue
            if int(person[4]) >= int(order[7]):
                count += 1
        answer.append(count)
                
    return answer