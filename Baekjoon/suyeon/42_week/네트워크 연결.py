import sys

input = sys.stdin.readline


# 집합을 하나로 합침
def union(parent, x, y): 
  x_root = find(parent, x)
  y_root = find(parent, y)
  parent[y_root] = x_root


# 집합의 대표번호를 반환
def find(parent, x): 
  if parent[x] != x:
    parent[x] = find(parent, parent[x])
  return parent[x]

  
# union-find 초기화
def init_union_find():
  return [i for i in range(n + 1)] 
  

n, m = int(input()), int(input())

# 크루스칼 알고리즘 - 비용에 따라 오름차순 정렬
edges = sorted([tuple(map(int, input().split())) for _ in range(m)], key=lambda x:x[2])

answer = 0
parent = init_union_find()

for a, b, cost in edges:
  if find(parent, a) != find(parent, b):
    union(parent, a, b)
    answer += cost

print(answer)