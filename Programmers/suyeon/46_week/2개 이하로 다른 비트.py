def solution(numbers):
    answer = []

    for number in numbers:
        if number % 2 == 0:
            answer.append(number + 1)
            continue
        
        bin_number = list('0' + bin(number)[2:])
        idx = ''.join(bin_number).rfind('0')
        
        bin_number[idx] = '1'
        bin_number[idx+1] = '0'
        
        answer.append(int(''.join(bin_number), 2))

    return answer