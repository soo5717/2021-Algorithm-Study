from collections import deque

SHEEP, WOLF = 0, 1

def bfs(graph, info, start):
    # 현재 노드, 양의 수, 늑대의 수, 이동 가능 노드
    max_sheep = 0
    queue = deque([[start, 1, 0, set()]])
    
    while queue:
        node, sheep_count, wolf_count, nexts = queue.popleft()
        
        max_sheep = max(max_sheep, sheep_count)
        nexts.update(graph[node])
        
        for next_node in nexts:
            if info[next_node] == SHEEP:
                queue.append([next_node, sheep_count + 1, wolf_count, nexts - {next_node}])
            elif sheep_count > wolf_count + 1:
                queue.append([next_node, sheep_count, wolf_count + 1, nexts - {next_node}])
            
    return max_sheep


def solution(info, edges):
    graph = [[] for _ in range(len(info))]
    
    for parent, child in edges:
        graph[parent].append(child)
    
    return bfs(graph, info, 0)