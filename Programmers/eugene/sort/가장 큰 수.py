def solution(numbers):
    answer = ''
    
    numbers=list(map(str, numbers))
    sort=sorted(numbers, key=lambda x:x*3, reverse=True)

    return str(int(''.join(sort)))