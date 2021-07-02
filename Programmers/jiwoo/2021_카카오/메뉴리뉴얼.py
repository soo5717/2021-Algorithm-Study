from collections import Counter
from itertools import combinations

def solution(orders, course):
    result = []

    for course_size in course:
        order_combinations = []
        for order in orders:
            order_combinations += combinations(sorted(order), course_size)

        most_ordered = Counter(order_combinations).most_common()
        result += [menu for menu, count in most_ordered if count > 1 and count == most_ordered[0][1]]

    return [''.join(menu) for menu in sorted(result)]