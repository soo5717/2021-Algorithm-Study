def solution(priorities, location):
    answer = 0

    while priorities:
        max_pri = max(priorities)
        n = priorities.pop(0)
        if max_pri == n:
            answer += 1
            if location == 0:
                return answer
            else:
                location -= 1
        else:
            priorities.append(n)
            if location == 0:
                location = len(priorities)-1
            else:
                location -= 1