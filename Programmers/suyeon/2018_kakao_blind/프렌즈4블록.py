def get_pop(m, n, board):
    set_pop = set()
    for i in range(1, n):
        for j in range(1, m):
            if board[i][j] == board[i - 1][j - 1] == board[i - 1][j] == board[i][j - 1]:
                if board[i][j] != '':
                    set_pop.update([(i, j), (i - 1, j - 1), (i - 1, j), (i, j - 1)])
    
    for i, j in set_pop:
        board[i][j] = ''
        
    for i in range(n):
        temp1 = [b for b in board[i] if b != '']
        temp2 = [''] * (m - len(temp1))
        board[i] = temp2 + temp1
        
    return len(set_pop)

def solution(m, n, board): 
    board = list(map(list, zip(*board))) # row, col rotation
    
    answer = 0
    while True:
        pop = get_pop(m, n, board)
        if not pop: return answer
        answer += pop