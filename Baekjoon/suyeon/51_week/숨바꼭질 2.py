from collections import deque

MAX_LENGTH = 100_001


def bfs(start, visited):
    if n >= k:
        return n - k, 1

    count = 0

    queue = deque([start])
    visited[start] = 0

    while queue:
        x = queue.popleft()

        if x == k:
            count += 1
            continue

        for nx in (x * 2, x + 1, x - 1):
            if nx < 0 or nx >= MAX_LENGTH or nx >= 2 * k:
                continue

            if visited[nx] == -1 or visited[nx] == visited[x] + 1:  # 첫 방문 or 시간 같은 경우
                visited[nx] = visited[x] + 1
                queue.append(nx)

    return visited[k], count


n, k = map(int, input().split())

min_time, min_count = bfs(n, [-1] * MAX_LENGTH)

print(min_time)
print(min_count)

