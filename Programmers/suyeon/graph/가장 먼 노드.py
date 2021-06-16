from heapq import heappop, heappush

INF = int(1e9)

def solution(n, edge):
    graph = [[] for _ in range(n + 1)]
    distance = [INF] * (n + 1)
    
    for node1, node2 in edge:
        graph[node1].append((node2, 1))
        graph[node2].append((node1, 1))
    
    queue = []
    heappush(queue, (0, 1)) # 1번 노드부터 시작
    distance[1] = 0
    while queue:
        dist, now = heappop(queue)
        if distance[now] < dist:
            continue
        for i in graph[now]:
            cost = dist + i[1]
            
            if cost < distance[i[0]]:
                distance[i[0]] = cost
                heappush(queue, (cost, i[0]))
            
    return distance.count(max(distance[1:]))