def rotate(key, M):
    rota_key = [[0] * M for _ in range(M)]

    for i in range(M):
        for j in range(M):
            rota_key[j][M-1-i] = key[i][j]
    return rota_key

def check(key, lock, exp_size, start_x, start_y, start, end):
    expend_ = [[0] * exp_size for _ in range(exp_size)]

    # expend_에 key 추가
    for i in range(start+1):
        for j in range(start+1):
            expend_[start_x+i][start_y+j] += key[i][j]

    for i in range(start, end):
        for j in range(start, end):
            expend_[i][j] += lock[i-start][j-start]
            if expend_[i][j] != 1:
                return False
    return True

def solution(key, lock):
    start = len(key) - 1
    end = start + len(lock)
    exp_size = len(lock) + start*2

    for _ in range(4):
        for i in range(end):
            for j in range(end):
                if check(key, lock, exp_size, i, j, start, end):
                    return True
        key = rotate(key, start+1)

    return False