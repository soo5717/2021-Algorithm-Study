from itertools import permutations

def operation(num1, num2, operator):
    if operator == '+':
        return num1 + num2
    if operator == '-':
        return num1 - num2
    if operator == '*':
        return num1 * num2
    
def calculate(exp, operator):
    array = []
    temp = ""
    for i in exp:
        if i.isdigit() == True:
            temp += i
        else:
            array.append(int(temp))
            array.append(i)
            temp = ""
    array.append(int(temp))
    
    for op in operator:
        stack = []
        while len(array) != 0:
            temp = array.pop(0)
            if temp == op:
                stack.append(operation(stack.pop(), array.pop(0), op))
            else:
                stack.append(temp)
        array = stack
            
    return abs(int(array[0]))

def solution(expression):
    operators = ['+', '-', '*']
    operators = list(permutations(operators, 3))
    result = []
    for i in operators:
        result.append(calculate(expression, i))
    return max(result)