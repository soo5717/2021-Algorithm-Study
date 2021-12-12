def parse_s(s):
    return [list(map(int, sub_s.split(','))) for sub_s in s[2:-2].split('},{')]


def solution(s):
    answer = {}
        
    for sub_list in sorted(parse_s(s), key=len): 
        for digit in sub_list:
            if digit not in answer:
                answer[digit] = 0
    
    return list(answer)