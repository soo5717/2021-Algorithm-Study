def solution(key, lock):
    m,n=len(key),len(lock)
    case_turn=turn(key,m)
            
    for case in case_turn:
        for i in range(n+m-1):
            for j in range(n+m-1):
                if check(case,lock,i,j,m,n): return True
    return False

def check(key, lock, x, y, m, n):
    
    #lock 중앙 배치의 확장 base
    base=[ [0]*(n+2*(m-1)) for _ in range(n+2*(m-1))]
    
    for i in range(n):
        for j in range(n):
            base[m+i-1][m+j-1]=lock[i][j]

    #base에 key값 더하기 
    for i in range(m):
        for j in range(m):
            base[x+i][y+j]+=key[i][j]

    #base의 lock 영역을 돌면서 1이 아닌 값이 있는지 체크. 
    start = m-1
    end = start+n
    for i in range(start, end):
        for j in range(start,end):
            if base[i][j] != 1: return False
    return True
    
def turn(key,m): #회전하는 모든 경우
    case_turn=[]
    for _ in range(4):
        case=[]
        for i in range(m):
            case+= [[key[m-j-1][i] for j in range(m)]]
        case_turn+=[case]
        key=case
    return case_turn
