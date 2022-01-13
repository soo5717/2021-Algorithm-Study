import sys

input = sys.stdin.readline


def tornado(move_count, direction):
    global answer, sx, sy

    for _ in range(move_count):
        dx, dy = move[direction]
        sx, sy = sx + dx, sy + dy

        if sx < 0 or sy < 0:
            break

        spreads = 0
        for dx, dy, rate in rates[direction]:
            nx, ny = sx + dx, sy + dy
            if not rate:
                sand = sand_matrix[sx][sy] - spreads
            else:
                sand = int(sand_matrix[sx][sy] * rate)

            if 0 <= nx < N and 0 <= ny < N:
                sand_matrix[nx][ny] += sand
            else:
                answer += sand
            spreads += sand


if __name__ == "__main__":
    N = int(input())
    sand_matrix = [list(map(int, input().split())) for _ in range(N)]

    answer = 0
    sx, sy = N // 2, N // 2  # 시작 지점 초기화
    move = {"left": (0, -1), "right": (0, 1), "up": (-1, 0), "down": (1, 0)}

    left = [
        (-2, 0, 0.02), (2, 0, 0.02), (-1, -1, 0.1), (-1, 0, 0.07), (-1, 1, 0.01),
        (1, -1, 0.1), (1, 0, 0.07), (1, 1, 0.01), (0, -2, 0.05), (0, -1, 0)
    ]
    right = [(dx, -dy, rate) for dx, dy, rate in left]
    down = [(-dy, dx, rate) for dx, dy, rate in left]
    up = [(-dx, dy, rate) for dx, dy, rate in down]
    rates = {'left': left, 'right': right, 'down': down, 'up': up}

    for i in range(N):
        if i % 2 == 0:
            tornado(i + 1, "left")
            tornado(i + 1, "down")
        else:
            tornado(i + 1, "right")
            tornado(i + 1, "up")

    print(answer)
