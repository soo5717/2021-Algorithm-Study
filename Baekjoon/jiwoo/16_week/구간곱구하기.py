import sys
from math import *

input = sys.stdin.readline
NUM = 1000000007

def update(node, start, end, index, value):
    if index < start or end < index:
        return
    if start == end:
        tree[node] = value
        return
    mid = (start+end) // 2
    update(node*2, start, mid, index, value)
    update(node*2+1, mid+1, end, index, value)
    tree[node] = (tree[node*2] * tree[node*2+1]) % NUM
    return tree[node]
    
def query(node, start, end, left, right):
    if right < start or end < left:
        return 1
    if left <= start and end <= right:
        return tree[node] % NUM
    
    mid = (start+end) // 2
    return query(node*2, start, mid, left, right) * query(node*2+1, mid+1, end, left, right) % NUM

N, M, K = map(int, input().split())
tree_size = 2**(ceil(log2(N)) + 1)

tree = [1] * tree_size
for i in range(N):
    num = int(input())
    update(1, 0, N-1, i, num)

for _ in range(M+K):
    a, b, c = map(int, input().split())
    if a == 1:
        update(1, 0, N-1, b-1, c)
    elif a == 2:
        print(query(1, 0, N-1, b-1, c-1))