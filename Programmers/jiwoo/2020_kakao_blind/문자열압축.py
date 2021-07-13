def solution(s):
    answer = len(s)
    zip_str = ''
    
    if answer == 1:
        return 1
    
    for slice_count in range(1, len(s)//2+1):
        zip_count = 1
        temp = s[:slice_count]
        for i in range(0, len(s), slice_count):
            if s[i:i+slice_count] == temp:
                    zip_count += 1
            else:
                if zip_count == 1:
                    zip_count = ''
                zip_str += str(zip_count) + temp
                temp = s[i:i+slice_count]
                zip_count = 1
        if zip_count == 1:
            zip_count = ''
        zip_str += str(zip_count) + temp
        
        if answer > len(zip_str):
            answer = len(zip_str)
        zip_str = ''  
        
    return answer