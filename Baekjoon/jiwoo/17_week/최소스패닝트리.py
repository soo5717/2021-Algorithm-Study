from sys import stdin

def union(a, b):
    a = find(a)
    b = find(b)

    if b < a:
        parent[a] = b
    else:
        parent[b] = a

def find(a):
    if a == parent[a]:
        return a
    parent[a] = find(parent[a])  # 경로 압축
    return parent[a]

input = stdin.readline
V, S = map(int, input().split())

edge = []
for _ in range(S):
    a, b, w = map(int, input().split())
    edge.append((w, a, b))

edge.sort(key=lambda x: x[0])

parent = list(range(V + 1))

sum = 0
for w, s, e in edge:
    if find(s) != find(e):
        union(s, e)
        sum += w

print(sum)