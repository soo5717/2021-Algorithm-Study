import sys
from collections import deque
from itertools import permutations

input = sys.stdin.readline


def solution(prev, count, hp, visited):
    if count == 0:
      x, y = milk[prev]
      distance = abs(home[0] - x) + abs(home[1] - y)
      
      if distance <= hp:
        return True
      return False

    if hp <= 0:
      return False

    for idx in range(len(milk)):
      if not visited[idx]:
        visited[idx] = True
        
        x, y = milk[idx]
        p_x, p_y = None, None
        
        if prev == -1: # 처음 시작일 경우
          p_x, p_y = home[0], home[1]
        else: # 중간 단계일 경우
          p_x, p_y = milk[prev][0], milk[prev][1]

        distance = abs(p_x - x) + abs(p_y - y)
        if distance <= hp:
          if solution(idx, count - 1, hp - distance + h, visited):
            return True
        visited[idx] = False
          
  

n, m, h = map(int, input().split())

town = []

home = None
milk = []

for row in range(n):
  temp = list(map(int, input().split()))
  town.append(temp)
  
  for col in range(n):
    if temp[col] != 0:
      if temp[col] == 2:
        milk.append((row, col))
      else:
        home = (row, col)

answer = 0
visited = [False] * len(milk)

for count in range(len(milk), 0, -1):
  if solution(-1, count, m, visited):
    answer = count
    break

print(answer)