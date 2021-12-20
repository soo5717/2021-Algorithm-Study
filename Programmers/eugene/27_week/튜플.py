def solution(s):
    answer, result = [], []
    
    s_split = s[2:-2].split("},{")
    for i in range(len(s_split)):
        answer.append(s_split[i].split(","))
            
    prev = set()
    for ans in sorted(answer, key=len):
        set_ans = set(ans)
        result.append(list(set_ans - prev)[0])
        prev = set_ans

    result = list(map(int,result))
    return result
