from heapq import heappush, heappop

INF = int(1e9)


def dijkstra(start, n, graph):
    distance = [INF] * (n + 1)
    distance[start] = 0
    
    queue = []
    heappush(queue, (0, start))
    
    while queue:
        dist, now = heappop(queue)
        
        if distance[now] < dist: 
            continue
        
        for c, node in graph[now]:
            cost = dist + c
            
            if cost < distance[node]:
                distance[node] = cost
                heappush(queue, (cost, node))
                
    return distance
    

def solution(N, road, K):
    graph = [[] for _ in range(N + 1)] 
    
    for a, b, c in road:
        graph[a].append((c, b))
        graph[b].append((c, a))
    
    return len([dist for dist in dijkstra(1, N, graph) if dist <= K])