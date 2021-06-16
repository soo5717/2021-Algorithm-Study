def solution(n, edges):
    graph = [[] for _ in range(n+1)]
    distance = [0]*(n+1)
    visited = [0]*(n+1)
    queue = [1]
    visited[1] = 1
    for (a,b) in edges:
        graph[a].append(b)
        graph[b].append(a)
    while queue:
        i = queue.pop(0)
        for j in graph[i]:
            if visited[j] == 0:
                visited[j] = 1
                queue.append(j)
                distance[j] = distance[i] + 1
    return distance.count(max(distance))