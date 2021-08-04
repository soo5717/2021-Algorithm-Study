import sys

input = sys.stdin.readline
DEFAULT_NUM = 1
DIVIDE_NUM = 1_000_000_007


# Bottom - Up 방식
def update(target, value):
    # target에 value 반영
    node = s + target - 1
    tree[node] = value
    # Root에 도달할 때까지 반복문 돌기 (좌측, 우측의 곱을 노드에 저장)
    node //= 2
    while node > 0:
        tree[node] = (tree[node * 2] * tree[node * 2 + 1]) % DIVIDE_NUM
        node //= 2


# Top - Down 방식
def query(left, right, node, query_left, query_right):
    # 연관 없음 -> 결과에 영향이 없는 값 return
    if query_right < left or right < query_left:
        return DEFAULT_NUM
    # 판단 가능 -> 현재 노드 값 return
    elif query_left <= left and right <= query_right:
        return tree[node]
    # 판단 불가 -> 자식에게 위임, 자식에서 올라온 값의 곱을 return
    mid = (left + right) // 2
    left_result = query(left, mid, node * 2, query_left, query_right)
    right_result = query(mid + 1, right, node * 2 + 1, query_left, query_right)
    return (left_result * right_result) % DIVIDE_NUM


n, m, k = map(int, input().split())  # 개수, 변경, 구간 곱
s = 1
while s < n:
    s *= 2

# init tree
tree = [DEFAULT_NUM] * (2 * s)
for i in range(n):
    tree[s + i] = int(input())
for i in range(s - 1, 0, -1):
    tree[i] = (tree[i * 2] * tree[i * 2 + 1]) % DIVIDE_NUM

for _ in range(m + k):
    a, b, c = map(int, input().split())
    if a == 1:
        update(b, c)
    else:
        print(query(1, s, 1, b, c))
