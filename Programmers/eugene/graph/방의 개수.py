import collections

def solution(arrows):
    
    move = [(-1, 0), (-1, 1), (0, 1), (1, 1), (1, 0), (1, -1), (0, -1), (-1, -1)]
    now = (0,0)
    
    visited = collections.defaultdict(int) #노드 방문 체크
    visited_dir = collections.defaultdict(int) #노드 간 경로 방문 체크
    queue = collections.deque([now])
    
    for arr in arrows:
        for _ in range(2):
            buf = (now[0]+move[arr][0], now[1]+move[arr][1])
            queue.append(buf)
            now=buf
            
    now = queue.popleft()
    visited[now] = 1
    cnt=0
    
    while queue:
        next = queue.popleft()
        if visited[next] == 1:
            if visited_dir[(now, next)] == 0:
                cnt += 1
        else:
            visited[next] = 1
            
        visited_dir[(now, next)] = 1
        visited_dir[(next, now)] = 1
        now = next
        
    return cnt
