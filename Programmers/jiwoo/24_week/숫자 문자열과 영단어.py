def solution(string):
    answer = ''
    word = ''
    num_numbers = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
    num_strings = ["zero", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]
    
    for s in string:
        if s.isdigit():
            answer += s
        elif s.isalpha():
            word += s
            if word in num_strings:
                index = num_strings.index(word)
                answer += str(num_numbers[index])
                word = ''
        
    return int(answer)