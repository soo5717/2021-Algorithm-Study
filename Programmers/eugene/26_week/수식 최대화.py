from collections import deque
import copy

def solution(expression):
    answer = 0
    operator_case = [["+", "-", "*"], ["+", "*", "-"], 
            ["-", "+", "*"],["-", "*", "+"],
            ["*", "+", "-"],["*", "-", "+"]]
    
    temp=""
    operand, operator= [], []
    for e in expression:
        if not e.isdigit():
            operand.append(temp)
            operator.append(e)
            temp = ""
        else:
            temp += e
    operand.append(temp)
    
    max_num = 0
    for case in operator_case:
        temp_operand = copy.deepcopy(operand)
        temp_operator = copy.deepcopy(operator)

        for c in case:
            while c in temp_operator:
                idx = temp_operator.index(c)
                temp_operand[idx] = str(eval(temp_operand[idx]+ c+temp_operand[idx+1]))
                
                del temp_operand[idx+1]
                del temp_operator[idx]
                
        max_num = max(max_num, abs(int(temp_operand[0])))
    return max_num
