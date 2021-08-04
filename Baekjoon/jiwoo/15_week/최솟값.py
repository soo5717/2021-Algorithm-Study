import sys

input = sys.stdin.readline
max_ = 1000000000

def query(left, right, node, query_left, query_right):
    if query_right < left or right < query_left:
        return max_
    elif query_left <= left and right <= query_right:
        return tree[node]
    else:
        mid = (left+right) // 2
        left_result = query(left, mid, node*2, query_left, query_right)
        right_result = query(mid+1, right, node*2+1, query_left, query_right)
        return min(left_result, right_result)

N, M = map(int, input().split())
size = 1
while size < N:
    size *= 2

#init tree
tree = [max_] * (size * 2)

for i in range(N):
    tree[size+i] = int(input())
for i in range(size-1, 0, -1):
    tree[i] = min(tree[i*2], tree[i*2+1])

for _ in range(M):
    a, b = map(int, input().split())
    print(query(1, size, 1, a, b))