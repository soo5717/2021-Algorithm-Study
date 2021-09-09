import sys

input = sys.stdin.readline
move = [(-1, 0), (1, 0), (0, -1), (0, 1)]  # (dx, dy) 상, 하, 좌, 우


def get_sea_point():
    sea_point = []
    for r in range(R):
        for c in range(C):
            if matrix[r][c] == '.':
                continue

            count = 0
            for dx, dy in move:
                nx = r + dx
                ny = c + dy

                if nx < 0 or ny < 0 or nx >= R or ny >= C:
                    count += 1
                elif matrix[nx][ny] == '.':
                    count += 1

            if count >= 3:
                sea_point.append((r, c))
            else:
                get_minimum(r, c)

    return sea_point


def get_minimum(r, c):
    global start_row, end_row, start_col, end_col
    if start_row > r:
        start_row = r
    if end_row < r:
        end_row = r
    if start_col > c:
        start_col = c
    if end_col < c:
        end_col = c


if __name__ == '__main__':
    R, C = map(int, input().split())
    matrix = [list(input().strip()) for _ in range(R)]

    start_row, end_row, start_col, end_col = R - 1, 0, C - 1, 0
    for x, y in get_sea_point():
        matrix[x][y] = '.'

    for m in matrix[start_row:end_row + 1]:
        print(''.join(m[start_col:end_col + 1]))
