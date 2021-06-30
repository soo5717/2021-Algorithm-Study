from collections import defaultdict, deque

def solution(arrows):
    move = [(-1, 0), (-1, 1), (0, 1), (1, 1), 
            (1, 0), (1, -1), (0, -1), (-1, -1)]
    now = (0, 0) # x(열), y(행)
    
    visited = defaultdict(int)
    visited_dir = defaultdict(int) # (A, B)는 A -> B
    
    queue = deque([now])
    for arrow in arrows:
        for _ in range(2): # 모래 시계 예외 처리를 위함
            next = (now[0] + move[arrow][0], now[1] + move[arrow][1])
            queue.append(next)
            now = next
            
    answer = 0
    now = queue.popleft()
    visited[now] = 1
    
    while queue:
        next = queue.popleft()
        
        if visited[next] == 1:
            if visited_dir[(now, next)] == 0:
                answer += 1
        else:
            visited[next] = 1
        
        visited_dir[(now, next)] = 1
        visited_dir[(next, now)] = 1
        now = next

    return answer