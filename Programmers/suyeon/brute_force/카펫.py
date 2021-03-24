def solution(brown, yellow):
    total = brown + yellow
    for x in range (3, total // 3 + 1):
        if total % x == 0 and brown ==  2 * (x + total // x - 2):
            return [total // x, x]