def solution(s):
    length_s = len(s)
    answer = [length_s]
    for i in range(1, length_s//2 + 1): # 절반
        count, length = 1, 0 
        for j in range(0, length_s - i, i):
            if s[j:j + i] != s[j + i:j + i + i]:
                length += i
                if count != 1:
                    length += len(str(count))
                count = 1
            else:
                count += 1
                
        if count == 1:
            length += i if length_s % i == 0 else length_s % i
        else:
            length += len(str(count)) + i
            
        answer.append(length)
        
    return min(answer)