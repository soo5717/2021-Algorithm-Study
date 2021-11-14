import sys
from collections import deque


def bfs(graph, start):
    queue = deque([start])
    visited[start] = True
    cnt_virus = 0
    while queue:
        v = queue.popleft()
        for idx in graph[v]:
            if not visited[idx]:
                queue.append(idx)
                visited[idx] = True
                cnt_virus += 1
    return cnt_virus


node_n, edge_n = int(input()), int(input())

visited = [False] * (node_n+1)
graph = [[] for _ in range(node_n + 1)]

for _ in range(edge_n):
    start, end = map(int, sys.stdin.readline().split())
    graph[start].append(end)
    graph[end].append(start)

print(bfs(graph, 1))
