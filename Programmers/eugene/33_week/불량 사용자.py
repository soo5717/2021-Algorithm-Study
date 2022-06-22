from itertools import product

def solution(user_id, banned_id):
    answer = 0
    temp_id = []

    candi = [[] for _ in banned_id]
    exclude_list = []
    
    for idx, b_id in enumerate(banned_id):
        for u_id in user_id:
            if len(b_id) != len(u_id):
                continue
            temp_id = list(u_id)
            for i in range(len(b_id)):
                if b_id[i] == '*':                
                    temp_id[i] = '*'
            if ''.join(temp_id) == b_id:
                candi[idx] += [u_id]
                
    candi_case = []
    all_case = list(product(*candi))
    for case in all_case:
        set_case = set(case)
        if len(set_case) != len(candi):
            continue
        if set_case not in candi_case:
            candi_case.append(set_case)

    return len(candi_case)
