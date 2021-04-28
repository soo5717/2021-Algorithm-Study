from collections import deque

def bfs(graph, start, visited):
    queue = deque([start])
    visited[start] = True
    
    while queue:
        v = queue.popleft()
        for i, connection in enumerate(graph[v]):
            if not visited[i] and connection == 1:
                queue.append(i)
                visited[i] = True

def solution(n, computers):
    answer = 0
    visited = [False] * n
    
    for i in range(n):
        if not visited[i]:
            answer += 1
            if sum(computers[i]) > 1:
                bfs(computers, i,visited)   
    return answer