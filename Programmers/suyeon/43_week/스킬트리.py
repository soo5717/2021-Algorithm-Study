import re

def solution(skill, skill_trees):
    answer = 0
    
    for skill_tree in skill_trees:
        temp = re.findall('['+skill+']', skill_tree)
        
        if ''.join(temp) == skill[:len(temp)]:
            answer += 1  
            
    return answer