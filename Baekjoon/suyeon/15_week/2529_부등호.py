# backtracking
MIN_NUM = 9999999999
MAX_NUM = 0


def backtracking(first, idx, answer):
    if idx == len(inequalities):
        global MIN_NUM, MAX_NUM
        answer = int(answer + str(first))
        if answer < MIN_NUM:
            MIN_NUM = answer
        if answer > MAX_NUM:
            MAX_NUM = answer
        return

    numbers[first] = True
    for second in range(10):
        if not numbers[second]:
            if inequalities[idx] == '<' and first < second:
                backtracking(second, idx + 1, answer + str(first))
            if inequalities[idx] == '>' and first > second:
                backtracking(second, idx + 1, answer + str(first))
    numbers[first] = False


k = int(input())
inequalities = list(map(str, input().split()))
numbers = [False] * 10  # 0 ~ 9

for i in range(10):
    backtracking(i, 0, '')

print(str(MAX_NUM).zfill(k + 1))
print(str(MIN_NUM).zfill(k + 1))
