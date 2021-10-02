import sys

N = int(input())
sand_per_tornado_left = [
    [0, 0, 0.02, 0, 0],
    [0, 0.1, 0.07, 0.01, 0],
    [0.05, 0, 0, 0, 0],
    [0, 0.1, 0.07, 0.01, 0],
    [0, 0, 0.02, 0, 0]
]
sand_per_tornado_right = [
    [0, 0, 0.02, 0, 0],
    [0, 0.01, 0.07, 0.1, 0],
    [0, 0, 0, 0, 0.05],
    [0, 0.01, 0.07, 0.1, 0],
    [0, 0, 0.02, 0, 0]
]
sand_per_tornado_down = [
    [0, 0, 0, 0, 0],
    [0, 0.01, 0, 0.01, 0],
    [0.02, 0.07, 0, 0.07, 0.02],
    [0, 0.1, 0, 0.1, 0],
    [0, 0, 0.05, 0, 0]
]
sand_per_tornado_up = [
    [0, 0, 0.05, 0, 0],
    [0, 0.1, 0, 0.1, 0],
    [0.02, 0.07, 0, 0.07, 0.02],
    [0, 0.01, 0, 0.01, 0],
    [0, 0, 0, 0, 0]
]

map_ = [list(map(int, input().split())) for _ in range(N)]

moving = [(0, -1), (1, 0), (0, 1), (-1, 0)]

# start index
x = (N // 2, N // 2)

time = 0
output_sand = 0

def tornado_move(sand_per_tornado):
    output = 0
    fly_sand = 0
    y_mount = map_[dx][dy]
    for mi in range(-2, 3):
        for mj in range(-2, 3):
            temp = int(sand_per_tornado[mi + 2][mj + 2] * y_mount)
            if (-1 < dx + mi < N) & (-1 < dy + mj < N):
                map_[dx + mi][dy + mj] += temp
                fly_sand += temp
            else:
                output += temp
    # y 모래 -> 0
    map_[dx][dy] = 0

    # alpha 위치 모래
    alpha_x, alpha_y = dx + moving_x, dy + moving_y
    alpha = y_mount - fly_sand
    if (-1 < alpha_x < N) & (-1 < alpha_y < N):
        map_[alpha_x][alpha_y] += alpha - output
    else:
        output = alpha
    return output


tornado_end = False
while x != (0, 0):
    for i in range(4):
        moving_x, moving_y = moving[i]  # direction

        if i == 0:
            sand_per_tornado = sand_per_tornado_left
            time += 1
        elif i == 1:
            sand_per_tornado = sand_per_tornado_down
        elif i == 2:
            sand_per_tornado = sand_per_tornado_right
            time += 1
        else:
            sand_per_tornado = sand_per_tornado_up

        for _ in range(time):
            dx, dy = x[0] + moving_x, x[1] + moving_y   # y index
            output_sand += tornado_move(sand_per_tornado)
            # x 이동
            x = (dx, dy)
            if x == (0, 0):
                tornado_end = True
                break
        if tornado_end:
            break

print(output_sand)
