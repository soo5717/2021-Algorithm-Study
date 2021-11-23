def solution(s):
    answer = ""
    temp = ""
    
    num_dict = ["zero", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]
    
    for x in s:
        if x.isdigit():
            answer += x
        else:
            temp += x
            for i in range(10):
                if temp == num_dict[i]:
                    answer += str(i)
                    temp = ""
            
    return int(answer)
