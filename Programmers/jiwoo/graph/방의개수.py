from collections import defaultdict, deque

def solution(arrows):
    location = [(0, 1), (1, 1), (1, 0), (1, -1), 
                (0, -1), (-1, -1), (-1, 0), (-1, 1)]
    now = (0, 0)
    
    #visited: 노드 방문여부, visited_direction: 노드 방문경로여부 확인
    visited = defaultdict(int)
    visited_direction = defaultdict(int)
    
    #예외처리 위해 두칸씩 이동
    queue = deque([now])
    for arrow in arrows:
        for _ in range(2):
            next = (now[0] + location[arrow][0], now[1] + location[arrow][1])
            queue.append(next)
            now = next
    
    room_count = 0
    now = queue.popleft()
    visited[now] = 1
    
    while queue:
        next = queue.popleft()
        if visited[next] == 1:
            if visited_direction[(now, next)] == 0:
                room_count += 1
        else:
            visited[next] = 1
        #양쪽 간선 방문 체크
        visited_direction[(now, next)] = 1
        visited_direction[(next, now)] = 1
        now = next
        
    return room_count