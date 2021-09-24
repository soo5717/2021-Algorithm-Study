import sys
from itertools import combinations
input = sys.stdin.readline

if __name__ == "__main__":
    n, m = map(int, input().split())
    chicken = []
    house = []
    
    for i in range(n):
        var = input().split()
        for j in range(n):
            if var[j] == '1':
                house.append((i,j))
            if var[j] == '2':
                chicken.append((i,j))

    chicken_m = list(combinations(chicken, m))

    min_dis = sys.maxsize
    for i in range(len(chicken_m)):
        temp = 0
        for x, y in (house):
            c_street = sys.maxsize
            for j in range(m):
                c_street = min(c_street, abs(x - chicken_m[i][j][0]) + abs(y - chicken_m[i][j][1]))
            temp += c_street
        min_dis = min(temp, min_dis)
    print(min_dis)
