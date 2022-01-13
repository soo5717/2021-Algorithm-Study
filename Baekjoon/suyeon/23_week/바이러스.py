import sys
from collections import deque

input = sys.stdin.readline

START_INDEX = 1


def get_count_of_virus_computer(start):
    count_of_virus_computer = 0

    queue = deque([start])
    visited[start] = True

    while queue:
        v = queue.popleft()

        for i in network[v]:
            if not visited[i]:
                queue.append(i)
                visited[i] = True
                count_of_virus_computer += 1

    return count_of_virus_computer


if __name__ == "__main__":
    N = int(input())

    network = [[] for _ in range(N + 1)]
    visited = [False] * (N + 1)
    for _ in range(int(input())):
        a, b = map(int, input().split())
        network[a].append(b)
        network[b].append(a)

    print(get_count_of_virus_computer(START_INDEX))
