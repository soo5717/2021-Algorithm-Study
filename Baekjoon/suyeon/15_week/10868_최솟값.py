import sys

input = sys.stdin.readline
INF = int(1e9)


def query(left, right, node, query_left, query_right):
    # 연관 없음 -> 결과에 영향이 없는 값 return
    if query_right < left or right < query_left:
        return INF
    # 판단 가능 -> 현재 노드 값 return
    elif query_left <= left and right <= query_right:
        return tree[node]
    # 판단 불가 -> 자식에게 위임, 자식에서 올라온 값의 min을 return
    else:
        mid = (left + right) // 2
        left_result = query(left, mid, node * 2, query_left, query_right)
        right_result = query(mid + 1, right, node * 2 + 1, query_left, query_right)
        return min(left_result, right_result)


n, m = map(int, input().split())
s = 1
while s < n:
    s *= 2

# init tree
tree = [INF] * (2 * s)
for i in range(n):
    tree[s + i] = int(input())
for i in range(s - 1, 0, -1):
    tree[i] = min(tree[i * 2], tree[i * 2 + 1])
# print(tree)

for _ in range(m):
    a, b = map(int, input().split())
    print(query(1, s, 1, a, b))