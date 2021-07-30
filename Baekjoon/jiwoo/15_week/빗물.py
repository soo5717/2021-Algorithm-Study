if __name__ == "__main__":
    H, W = map(int, input().split())
    blocks = list(map(int, input().split()))

    rain_area = 0

    for i in range(W):
        left_high = max(blocks[:i+1])
        right_high = max(blocks[i:])

        height = min(left_high, right_high)
        rain_area += height - blocks[i]
    print(rain_area)