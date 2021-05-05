from functools import cmp_to_key

def solution(numbers):
    numbers = [str(number) for number in numbers]
    # 음수, 양수, 0
    numbers.sort(key=cmp_to_key(lambda x, y: int(y+x)-int(x+y)))
    return ''.join(numbers) if numbers[0] != '0' else '0'