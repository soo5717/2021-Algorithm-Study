if __name__ == "__main__":
    H,W = map(int, input().split())
    block=list(map(int, input().split()))
    answer=0

    for i in range(W):
        left=max(block[:i+1])
        right=max(block[i:])

        height=min(left, right)
        answer+= height-block[i]
    print(answer)
