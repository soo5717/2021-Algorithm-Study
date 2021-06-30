from collections import deque

INF = int(1e9)

def solution(n, edge):
    graph = [[] for _ in range(n + 1)]
    distance = [INF] * (n + 1)
    
    for node1, node2 in edge:
        graph[node1].append(node2)
        graph[node2].append(node1)
    
    queue = deque([])
    queue.append((0, 1)) # 1번 노드부터 시작 (dist, node)
    distance[1] = 0
    while queue:
        dist, now = queue.popleft()
        if distance[now] < dist:
            continue
        for node in graph[now]:
            cost = dist + 1
            
            if cost < distance[node]:
                distance[node] = cost
                queue.append((cost, node))
    return distance.count(max(distance[1:]))