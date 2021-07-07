from itertools import combinations 
from collections import defaultdict 
import bisect

def solution(info, query):
    answer = []
    people = defaultdict(list)
    
    for i in info:
        people_info = i.split()
        score = int(people_info[-1]) #점수
        people[''.join(people_info[:-1])].append(score)    

        for j in range(4): 
            combi = list(combinations(people_info[:-1], j)) 
            for c in combi: 
                people[''.join(c)].append(score) 
                  
    for i in people:            
        people[i].sort() #탐색을 위해 정렬
        
    for q in query: #쿼리 조건에 맞게 탐색
        key = q.split() 
        score = int(key.pop()) 
        key = ''.join(key) 
        key = key.replace('and', '').replace(' ', '').replace('-', '') #
        answer.append(len(people[key])-bisect.bisect_left(people[key], score))    
    return answer
