# 참고 코드라 코드 리뷰 후 한 번 더 해 볼 예정

import sys;

input = sys.stdin.readline

def sand_move(position, direction_ind, sand):
    rate = [2, 10, 7, 1, 5, 10, 7, 1, 2]
    sand_matrix = [
                   [(-2, 0), (-1, -1), (-1, 0), (-1, 1), (0, -2), (1, -1), (1, 0), (1, 1), (2, 0)],
                   [(0, -2), (1, -1), (0, -1), (-1, -1), (2, 0), (1, 1), (0, 1), (-1, 1), (0, 2)]
                   ]
    ret = 0
    y = sand[position[0]][position[1]]
    sand[position[0]][position[1]] = 0
    alpha = y
    for index, pos_tmp in enumerate(sand_matrix[direction_ind % 2]):
        r = position[0] + pos_tmp[0] * (-1) ** (direction_ind // 2)
        c = position[1] + pos_tmp[1] * (-1) ** (direction_ind // 2)
        temp = (y * rate[index]) // 100
        if temp:
            alpha -= temp
            if 0 <= r < N and 0 <= c < N:
                sand[r][c] += temp
            else:
                ret += temp
    r = position[0] + direction[direction_ind][0]
    c = position[1] + direction[direction_ind][1]
    if 0 <= r < N and 0 <= c < N:
        sand[r][c] += alpha
    else:
        ret += alpha
    return ret


N = int(input())
sand = [list(map(int, input().split())) for _ in range(N)]
check = [[0 for _ in range(N)] for _ in range(N)]
out_sand = 0

s = [N//2, N//2]
direction = [(0, -1), (1, 0), (0, 1), (-1, 0)] # l d r u
ind = 0
check[s[0]][s[1]] = 1
while s != [0, 0]:
    s[0] += direction[ind][0]
    s[1] += direction[ind][1]
    check[s[0]][s[1]] = 1
    
    out_sand += sand_move(s, ind, sand)
    
    ind = (ind+1) % 4
    if check[s[0] + direction[ind][0]][s[1] + direction[ind][1]]:
        ind = (ind-1) % 4
print(out_sand)