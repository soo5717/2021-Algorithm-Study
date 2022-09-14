def solution(s):
    s = [' '] + list(s.lower())
    
    for i in range(len(s) - 1):
        if s[i] == ' ' and not s[i + 1].isdigit():
            s[i + 1] = s[i + 1].upper()
            
    return ''.join(s[1:])