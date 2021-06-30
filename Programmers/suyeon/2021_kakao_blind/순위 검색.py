from collections import defaultdict

def solution(info, query):
    group_info = defaultdict(list)
    for i, user_info in enumerate(info):
        lang, task, exp, food, score = user_info.split()
        score = int(score)
        
        case_list = []
        for a in ["-", lang]:
            for b in ["-", task]:
                for c in ["-", exp]:
                    for d in ["-", food]:
                        group_info[(a, b, c, d)].append(score)
            
    for key in group_info:
        group_info[key].sort()
    
    answer = []
    for q in query:
        lang, _, task, _, exp, _, food, score = q.split()
        score = int(score)
        
        temp = group_info[(lang, task, exp, food)]
        
        start, end = 0, len(temp) - 1
        while start <= end:
            mid = (start + end) // 2
            
            if temp[mid] < score:
                start = mid + 1
            else:
                end = mid - 1
            
        answer.append(len(temp) - start) 
    return answer