import sys

input = sys.stdin.readline
combination_list = []


def get_min(n):
    answer = int(1e9)

    team = set(numbers)
    for start_team in combination_list:
        link_team = list(team - set(start_team))

        start, link = 0, 0
        for i in range(n):
            for j in range(i + 1, n):
                x1, y1 = start_team[i], start_team[j]
                start += matrix[x1][y1] + matrix[y1][x1]

                x2, y2 = link_team[i], link_team[j]
                link += matrix[x2][y2] + matrix[y2][x2]

        diff = abs(start - link)

        if diff < answer:
            answer = diff
        if not answer:
            break
    return answer


def combination(n, k, idx, current):
    global combination_list
    # 종료 조건
    if not k:
        combination_list.append(current)
        return
    if n == k:
        temp = current.copy()
        temp.extend(numbers[idx:])
        combination_list.append(temp)
        return

    # 값을 뽑는 경우
    temp = current.copy()
    temp.append(numbers[idx])
    combination(n - 1, k - 1, idx + 1, temp)
    # 값을 뽑지 않는 경우
    combination(n - 1, k, idx + 1, current)


N = int(input())

matrix = []
for _ in range(N):
    matrix.append(list(map(int, input().split())))

numbers = [i for i in range(N)]
combination(N, N // 2, 0, [])
print(get_min(N // 2))
