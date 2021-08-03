def move(idx, w, blocks):
    max_idx, max_height = idx, 0
    for i in range(idx + 1, w):
        if blocks[i] >= blocks[idx]:
            return i

        if blocks[i] >= max_height:
            max_height = blocks[i]
            max_idx = i
    return max_idx


def rain(idx, max_idx, blocks):
    total_rain = 0
    max_height = min(blocks[idx], blocks[max_idx])
    for i in range(idx + 1, max_idx):
        total_rain += max_height - blocks[i]
    return total_rain


def main():
    h, w = map(int, input().split())
    blocks = list(map(int, input().split()))

    idx, answer = 0, 0
    while idx < w - 1:
        max_idx = move(idx, w, blocks)
        answer += rain(idx, max_idx, blocks)
        idx = max_idx
    print(answer)


if __name__ == '__main__':
    main()
