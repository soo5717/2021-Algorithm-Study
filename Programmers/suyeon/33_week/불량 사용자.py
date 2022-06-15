from collections import defaultdict 

answer = []

def dfs(banned_list, idx, temp):
    if idx == len(banned_list):
        temp = set(temp)
        
        if temp not in answer:
            answer.append(temp)
            
        return
    
    for u_id in banned_list[idx]: 
        if u_id not in temp:
            temp.add(u_id)
            dfs(banned_list, idx + 1, temp) 
            temp.remove(u_id)
    

def is_mapping(u_id, b_id): 
    if len(u_id) != len(b_id):
        return False
    
    for u, b in zip(u_id, b_id):
        if b == '*':
            continue
        
        if u != b:
            return False
        
    return True


def solution(user_id, banned_id):
    banned_list = []
    
    for b_id in banned_id:
        banned_list.append([u_id for u_id in user_id if is_mapping(u_id, b_id)])
    
    dfs(banned_list, 0, set())
    
    return len(answer)