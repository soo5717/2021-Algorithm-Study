def solution(begin, target, words):
    answer = 0
    stacks=[begin] 
    if target not in words:
        return 0
    
    visited = [0 for i in words]
    
    while stacks:
        # 스택을 활용한 dfs 구현
        stack = stacks.pop()
        
        if stack == target:
             
            return answer
        
        for w in range(len(words)):
            # 조건 1. 한 개의 알파벳만 다른 경우
            if len([i for i in range(0,len(words[w])) if words[w][i]!=stack[i]]) == 1 and not visited[w]:               
                visited[w] = 1
                stacks.append(words[w])
        # depth +
        answer +=1
        
    if stack != target: #모든 스택을 돌고 나서도 target과 같지 않다면 0을 출력
        return 0
    return answer
