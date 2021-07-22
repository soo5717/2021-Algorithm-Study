from math import floor

def solution(str1, str2):
    str1 = str1.upper()
    str2 = str2.upper()

    str1_list = []
    str2_list = []

    for i in range(len(str1)-1):
        if str1[i:i+2].isalpha():
            str1_list.append(str1[i:i+2])

    for i in range(len(str2)-1):
        if str2[i:i+2].isalpha():
            str2_list.append(str2[i:i+2])

    intersection = set(str1_list) & set(str2_list)
    union = set(str1_list) | set(str2_list)

    if not union:
        return 65536

    intersection_count = sum([min(str1_list.count(e), str2_list.count(e)) for e in intersection])
    union_count = sum([max(str1_list.count(e), str2_list.count(e)) for e in union])

    return floor((intersection_count / union_count) * 65536)