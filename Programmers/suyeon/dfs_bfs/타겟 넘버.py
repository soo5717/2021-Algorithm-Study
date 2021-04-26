def solution(numbers, target):
    answers = [numbers[0], -numbers[0]]
    for number in numbers[1:]:
        temp = []
        for answer in answers:
            temp.append(answer + number)
            temp.append(answer - number)
        answers = temp
                  
    return answers.count(target)