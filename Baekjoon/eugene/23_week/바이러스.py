import sys

node_n, edge_n = int(input()), int(input())
graph = {}


def dfs(graph, startV):
    s = [startV]
    visited = []
    while s:
        nowV = s.pop()
        if nowV not in visited:
            visited.append(nowV)
            s.extend(graph[nowV][::-1])
    return len(visited)-1


for i in range(1, node_n+1):
    graph[str(i)] = []

for _ in range(edge_n):
    start, end = sys.stdin.readline().split()
    v1, v2 = graph[start], graph[end]
    v1.append(end)
    v2.append(start)

print(dfs(graph, '1'))
