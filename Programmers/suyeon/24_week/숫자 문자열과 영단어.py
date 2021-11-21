from collections import deque

word_dict = { 
    'zero': '0', 'one': '1', 'two': '2', 'three': '3', 'four': '4', 
    'five': '5', 'six': '6', 'seven': '7', 'eight': '8',  'nine': '9' 
}

def solution(s):
    s = deque(s)
    answer, word = '', ''
    
    while(s):
        digit = s.popleft()
        
        if digit.isdigit():
            answer += digit
            continue
            
        word += digit
        
        if word in word_dict:
            answer += word_dict[word]
            word = '' 
        
    return int(answer)