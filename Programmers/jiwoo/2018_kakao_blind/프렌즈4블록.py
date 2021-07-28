def solution(m, n, board):
    answer = 0
    for i in range(len(board)):
        board[i] = list(board[i])
    while True:
        remove = [[0] * n for _ in range(m)]
        for i in range(m-1):
            for j in range(n-1):
                if board[i][j] != 0 and board[i][j] == board[i][j+1] == board[i+1][j] == board[i+1][j+1]:
                    remove[i][j], remove[i][j+1], remove[i+1][j], remove[i+1][j+1] = 1, 1, 1, 1
        count = 0
        for i in range(m):
            count += sum(remove[i])
        answer += count
        if count == 0:
            break
        for i in range(m-1, -1, -1):
            for j in range(n):
                if remove[i][j] == 1:
                    x = i-1
                    while x >= 0 and remove[x][j] == 1:
                        x -= 1
                    if x < 0:
                        board[i][j] = 0
                    else:
                        board[i][j] = board[x][j]
                        remove[x][j] = 1
    return answer