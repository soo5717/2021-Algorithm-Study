def solution(n, left, right):
    answer = []
    
    start_i, start_j = left // n, left % n
    end_i, end_j = right // n, right % n
    
    i, j = start_i, start_j
    while True:
        answer.append(max(i, j)+1)
        
        if i == end_i and j == end_j:
            break
        
        if j >= n-1:
            i += 1
            j = 0
        else:
            j+=1

    return answer
