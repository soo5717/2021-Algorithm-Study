import sys

input = sys.stdin.readline

N, K = map(int, input().split())

children = list(map(int, input().split()))
print(sum(sorted([children[i] - children[i - 1] for i in range(1, N)])[:N - K]))