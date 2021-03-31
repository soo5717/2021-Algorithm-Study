def solution(brown, yellow):
    total = brown + yellow
    # x(세로) <= total//x(가로) 이고, 
    # x는 최소 3 이상이기 때문에 total//3 범위까지 반복함
    for x in range (3, total // 3 + 1):
        if total % x == 0 and brown ==  2 * (x + total // x - 2):
            return [total // x, x]