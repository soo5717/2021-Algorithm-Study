from itertools import combinations
import math

MAXNUM = 1000000000000001

def solution(line):
    case = list(combinations(line, 2))
    point_list = []
    
    min_x, min_y = MAXNUM , MAXNUM 
    max_x, max_y = -MAXNUM , -MAXNUM 
    for line1, line2 in case:
        a, b, e = line1
        c, d, f = line2
        
        den = a*d - b*c
        x_mol = b*f - e*d
        y_mol = e*c - a*f
        
        if den == 0:
            continue

        x, y = (b*f-e*d)/(a*d - b*c) , (e*c-a*f)/(a*d - b*c)
        if x.is_integer() and y.is_integer():
            point_list.append([int(x), int(y)])
            min_x, max_x = min(min_x, int(x)), max(max_x, int(x))
            min_y, max_y = min(min_y, int(y)), max(max_y, int(y))

    answer = [["."] * (abs(max_x - min_x)+1) for j in range(abs(max_y - min_y)+1)]
    
    # 2. 맵 그리기
    for point_x, point_y in point_list:
        x, y = abs(max_y - point_y), abs(min_x - point_x)
        answer[x][y] = '*'
        
    answer = [str(''.join(a)) for a in answer]
    return answer
