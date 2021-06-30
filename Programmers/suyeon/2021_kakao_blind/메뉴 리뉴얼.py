from collections import defaultdict
from itertools import combinations

def solution(orders, course):
    course_dict = {}
    for c in course:
        course_dict[c] = defaultdict(int)
    
    for order in orders:
        menu_list = list(order)
        for c in course:
            temp = list(combinations(menu_list, c))
            for t in temp:
                t = list(t)
                t.sort()
                course_dict[c][''.join(t)] += 1

    answer = []
    for key, value in course_dict.items():
        max_value = 0
        for k, v in value.items():
            if v > max_value:
                max_value = v
        for k, v in value.items():
            if v >= 2 and v == max_value:
                answer.append(''.join(k))

    answer.sort()
    return answer