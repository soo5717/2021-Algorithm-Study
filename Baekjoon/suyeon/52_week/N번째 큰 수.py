import sys
from heapq import heappush, heappop, heapify

n = int(input())

min_heap = list(map(int, sys.stdin.readline().split()))
heapify(min_heap)

for _ in range(n - 1):
    for num in map(int, sys.stdin.readline().split()):
        if min_heap[0] < num:
            heappop(min_heap)
            heappush(min_heap, num)

print(min_heap[0])
