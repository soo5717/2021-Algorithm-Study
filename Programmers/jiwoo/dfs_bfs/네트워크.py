def bfs(k, graph, visited):
    visited[k] = 1
    for i in range(len(graph[k])):
        if visited[i] == 0 and graph[k][i] == 1:
            bfs(i, graph, visited)

def solution(n, computers):
    network = 0
    visited = [0] * n

    while 0 in visited:
        i = visited.index(0)
        if visited[i] == 0:
            bfs(i, computers, visited)
            network += 1

    return network