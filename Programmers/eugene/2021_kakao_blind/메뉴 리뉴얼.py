from itertools import combinations
from collections import Counter

def solution(orders, course):
    final_set_menu = []
    
    
    for c in course: #각 개수의 조합 구하기
        set_menu_list=[]
        for order in orders: #손님이 시킨 메뉴에서
            set_menu_list += combinations(sorted(order), c)
        #최소 2명 이상의 손님으로부터 주문된 조합에 대해서만 후보에 포함.
        set_menu_list = Counter(set_menu_list).most_common()
        
        for set_menu,cnt in set_menu_list:
            if cnt >1 and cnt==set_menu_list[0][1]: #가장 많이 함께 주문한, 2명 이상의 손님이 주문한
                final_set_menu += [set_menu]
    
    
    return [''.join(menu) for menu in sorted(final_set_menu)]
