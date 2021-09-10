def get_lcs():
    lcs = [[0] * (len_first + 1) for _ in range(len_second + 1)]
    for i in range(1, len_second + 1):
        for j in range(1, len_first + 1):
            if first[j - 1] == second[i - 1]:
                lcs[i][j] = lcs[i - 1][j - 1] + 1
            else:
                lcs[i][j] = max(lcs[i - 1][j], lcs[i][j - 1])
    return lcs[-1][-1]


if __name__ == '__main__':
    first, second = input(), input()
    len_first, len_second = len(first), len(second)
    print(get_lcs())