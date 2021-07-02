from collections import deque

def solution(n, results):
    m=len(results)
    graph_lower = [[] for _ in range(n+1)]
    graph_upper = [[] for _ in range(n+1)]
    for i in range(m):
        a,b = results[i]
        graph_lower[a].append(b)
        graph_upper[b].append(a)
    
    result=[0]*(n)
    for i in range(1,n+1):
        indegree=[False]*(n+1)
        indegree[i] = True #시작 노드 방문 처리        
        cnt=0
        q1,q2=deque([i]),deque([i])
        while q1:
            now=q1.popleft()
            for next_node in graph_lower[now]:
                if indegree[next_node]==False:
                    indegree[next_node]=True
                    cnt+=1
                    q1.append(next_node)         
        while q2:
            now=q2.popleft()
            for next_node in graph_upper[now]:
                if indegree[next_node]==False:
                    indegree[next_node]=True
                    cnt+=1
                    q2.append(next_node)             
        
        result[i-1]+=cnt
        
    answer=0 
    for k in range(n):
        if result[k] == n-1:
            answer+=1
    return answer
