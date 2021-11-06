import copy
from itertools import combinations
from collections import deque

moving = [(-1, 0), (1, 0), (0, -1), (0, 1)]
empty_list, virus_list = [], []
lab_map = []


def bfs(new_map):
    visited = [[False] * col for _ in range(row)]
    queue = deque(virus_list)
    infect_cnt = 0
    while queue:
        vy, vx = queue.popleft()
        for i in range(4):
            mx = vx + moving[i][1]
            my = vy + moving[i][0]
            if my < 0 or my >= row or mx < 0 or mx >= col:
                continue
            if new_map[my][mx] == '0' and not visited[my][mx]:
                queue.append([my, mx])
                new_map[my][mx] = '2'
                visited[my][mx] = True
                infect_cnt += 1

    return len(empty_list) - infect_cnt - 3


row, col = map(int, input().split())
for i in range(row):
    temp = input().split()
    lab_map.append(temp)

    for j in range(col):
        if temp[j] == '0':
            empty_list.append([i, j])
        elif temp[j] == '2':
            virus_list.append([i, j])

max_safe_area = 0
for new_wall in list(combinations(empty_list, 3)):
    empty1, empty2, empty3 = new_wall
    y1, x1 = empty1
    y2, x2 = empty2
    y3, x3 = empty3

    new_map = copy.deepcopy(lab_map)
    new_map[y1][x1] = '1'
    new_map[y2][x2] = '1'
    new_map[y3][x3] = '1'

    safe_area = bfs(new_map)
    max_safe_area = safe_area if max_safe_area < safe_area else max_safe_area

print(max_safe_area)
