def solution(n, k):
    str_num = ''

    while n:
        str_num += str(n % k)
        n = n // k

    str_num = str_num[::-1]

    str_num_split = str_num.split('0')
    
    new_list = []
    for num in str_num_split:
        if len(num) > 0:
            new_list.append(num)
    str_num_split = list(map(int, new_list))

    count = 0
    for i in str_num_split:
        prime = True
        if i < 2:
            continue
        for j in range(2, int(i**0.5)+1):
            if i % j == 0:
                prime = False
                break
        if prime:
            count += 1

    return count