def solution(s):
    answer = []
    s = s[2:-2]
    s = s.split("},{")
    s.sort(key = len)
    for i in s:
        i = i.split(",")
        for j in i:
            if int(j) not in answer:
                answer.append(int(j))
    return answer