import math

NUM = 65536

def get_set(_str):
    _list = []
    for i in range(0, len(_str) - 1):
        e = _str[i:i + 2].lower()
        if 'a' <= e[0] <= 'z' and 'a' <= e[1] <= 'z':
            _list.append(e)
    return _list

def solution(str1, str2):
    str1, str2 = get_set(str1), get_set(str2)
    
    set_intersection = set(str1) & set(str2)
    set_union = set(str1) | set(str2)
    
    if not set_union:
        return NUM
    
    intersection = sum([min(str1.count(e), str2.count(e)) for e in set_intersection])
    union = sum([max(str1.count(e), str2.count(e)) for e in set_union])
    
    return math.floor(intersection * NUM / union)