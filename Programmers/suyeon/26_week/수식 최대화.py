import re
from functools import reduce
from itertools import permutations

PLUS, MINUS, MULTIPLY = '+', '-', '*'

def calculate(operator, numbers):
    if operator == PLUS:
        return reduce(lambda x, y: x + y, numbers)
    elif operator == MINUS:
        return reduce(lambda x, y: x - y, numbers)
    else:
        return reduce(lambda x, y: x * y, numbers)
        

def divide_and_conquer(operators, idx, expression):
    if expression.isdigit():
        return int(expression)
    
    temp = []
    for sub_expression in expression.split(operators[idx]):
        temp.append(divide_and_conquer(operators, idx + 1, sub_expression))
    
    return calculate(operators[idx], temp)
    

def solution(expression):  
    answer = 0
    
    for operators in permutations(set(re.sub(r'[0-9]', '',expression))):
        answer = max(answer, abs(divide_and_conquer(operators, 0, expression)))
        
    return answer