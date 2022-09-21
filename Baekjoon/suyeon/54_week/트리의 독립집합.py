import sys

input = lambda: sys.stdin.readline()


def dfs(start_node):
    # 노드 방문 체크
    visited[start_node] = True

    # 루트 포함만 dp 가중치 더하기 & path 추가
    dp[start_node][1] += weights[start_node]
    path[start_node][1].append(start_node)

    for node in tree[start_node]:
        if not visited[node]:
            sub_path = dfs(node)

            # 부모를 포함 하지 않을 시 -> 자식 포함 or 미포함 경우의 수
            dp[start_node][0] += max(dp[node][0], dp[node][1])
            path[start_node][0] += sub_path[0 if dp[node][0] > dp[node][1] else 1]

            # 부모를 포함할 경우 -> 자식 포함 할 수 없음
            dp[start_node][1] += dp[node][0]
            path[start_node][1] += sub_path[0]

    return path[start_node]


n = int(input())
weights = [0] + list(map(int, input().split()))

tree = [[] for _ in range(n + 1)]
visited = [False] * (n + 1)

# 0 - 루트 노드 미포함, 1 - 루트 노드 포함
dp = [[0, 0] for _ in range(n + 1)]  # 최대 독립 집합 크기
path = [[[], []] for _ in range(n + 1)]  # 독립 집합 원소

for _ in range(n - 1):
    a, b = map(int, input().split())

    tree[a].append(b)
    tree[b].append(a)

dfs(1)
idx = 0 if dp[1][0] > dp[1][1] else 1

print(dp[1][idx])
print(*sorted(path[1][idx]))
