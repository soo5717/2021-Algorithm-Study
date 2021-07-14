def get_rotation(keys, m): # 90 rotation
    matrix = [[0] * m for _ in range(m)]
    for i in range(m):
        for j in range(m):
            matrix[i][j] = keys[m - 1 - j][i]
    return matrix

def solution(keys, locks):
    m, n = len(keys), len(locks)
    for angle in range(0, 360, 90):
        for x in range(m + n):
            for y in range(m + n):
                matrix = [[0] * (n + 2 * m) for _ in range(n + 2 * m)]
                for i in range(m):
                    for j in range(m):
                        matrix[x + i][y + j] = keys[i][j]
                
                answer = True
                for i in range(n):
                    for j in range(n):
                        if matrix[m + i][m + j] ^ locks[i][j] == 0:
                            answer = False
                            break
                if answer: return True
                
        keys = get_rotation(keys, m)
    return False