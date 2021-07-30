def solution(m, n, board):
    answer = 0
    for b in range(m): board[b]=list(board[b])

    while True:
        index_list=[]
        for i in range(m-1):
            for j in range(n-1):
                if board[i][j] == board[i][j+1] == board[i+1][j] == board[i+1][j+1] != "0":
                    index_list+=[(i, j), (i, j+1),(i+1, j), (i+1, j+1)]
                    
       
        set_index_len= len(set(index_list))
        if set_index_len ==0: #지울 블록 없으면 종료
            break
        answer+=set_index_len
    
        for x,y in index_list: #지울 블록 지우기
            board[x][y]="0"

        for x,y in reversed(index_list):
            chk_drop=x-1
            while chk_drop >=0:
                if board[x][y]=="0" and board[chk_drop][y] !="0":
                    board[x][y]=board[chk_drop][y] #아래로 내리고
                    board[chk_drop][y]="0" #내린 부분 0으로 채우기
                    x-=1
                chk_drop-=1 #윗 줄로 올라가서 또 확인. 맨 윗줄까지      
    return answer
