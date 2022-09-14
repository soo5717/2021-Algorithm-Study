from collections import defaultdict, deque


def bfs(v1, v2, graph):
    count = 1
    queue = deque([v1])
    
    visited = [False] * (len(graph) + 1)
    visited[v1] = True
    visited[v2] = True
    
    while queue:
        node = queue.popleft()
        
        for n in graph[node]:
            if not visited[n]:
                visited[n] = True
                queue.append(n)
                count += 1
    
    return count
            

def solution(n, wires):
    answer = n 
    graph = defaultdict(set)
    
    for v1, v2 in wires:
        graph[v1].add(v2)
        graph[v2].add(v1)
        
    for v1, v2 in wires:
        answer = min(answer, abs(n - 2 * bfs(v1, v2, graph)))
        
    return answer