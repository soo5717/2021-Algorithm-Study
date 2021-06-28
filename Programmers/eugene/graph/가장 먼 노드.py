from collections import deque

def solution(n, edge):
    m=len(edge)
    graph=[[] for _ in range(n+1)]
    for i in range(m):
        a,b = edge[i]
        graph[a].append(b)
        graph[b].append(a)
    distance = [-1]*(n+1)
    distance[1] = 0
    q=deque([1])
    while q:
        now=q.popleft()
        for next_node in graph[now]:
            if distance[next_node]==-1:
                distance[next_node] = distance[now]+1
                q.append(next_node)
    
    k=max(distance)
    cnt=0
    for i in range(1,n+1):
        if distance[i] ==k:
            cnt+=1
            
    return cnt
