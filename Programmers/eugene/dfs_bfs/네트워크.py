def solution(n, computers):
    answer = 0
    visited = [False]*n
    
    for i in range(n):
        if visited[i] == False : #방문하지 않은 컴퓨터면 탐색
            dfs(computers, i, visited) #dfs함수 실행
            answer+=1
    return answer

def dfs(graph, v, visited):
    visited[v]=True

    for i in range(len(graph)):
        if graph[v][i] and not visited[i]: #현재 graph에서 연결되어 있고, 방문하지 않은 노드
            dfs(graph, i ,visited) #재귀함수
