def solution(n):
    answer = []
    triangle = [[0] * n for _ in range(n)]
    
    x, y = -1, 0
    number = 1
    
    for i in range(n):
        for j in range(i, n):
            if i % 3 == 0:
                x += 1
            elif i % 3 == 1:
                y += 1
            elif i % 3 == 2:
                x -= 1
                y -= 1
            triangle[x][y] = number
            number += 1

    for tri in triangle:
        for i in tri:
            if i != 0:
                answer.append(i)
        
    return answer