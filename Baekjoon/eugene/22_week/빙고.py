import sys

chulsu = [input().split() for _ in range(5)]
visited = [ [False] * 5  for _ in range(5)]
    
vertical = [False] * 5
horizontal = [False] * 5
diagonal = [False] * 2


def visit_bingo(number):
    for i in range(5):
        for j in range(5):
            if chulsu[i][j] == number:
                visited[i][j] = True
                return 


def check_bingo(matrix):
    for x in range(5):
        # Step1. Horizontal, x
        if all(matrix[x]):
            horizontal[x] = True
            
        #Step2. Vertical, y
        for y in range(5):
            if not matrix[y][x]:
                break
            if y == 4:
                vertical[x] = True

                    
            # Step3. diagonal
            if x == y :
                for i in range(5):
                    if not matrix[i][i]:
                        break
                    if i == 4:
                        diagonal[0] = True
            if x + y == 4:
                for i in range(5):
                    if not matrix[i][4-i]:
                        break
                    if i == 4:
                        diagonal[1] = True
                        

def cnt_bingo():
    cnt = 0
    for i in range(5):
        if vertical[i]:
            cnt += 1
        if horizontal[i]:
            cnt += 1

    for i in range(2):
        if diagonal[i]:
            cnt += 1
    return cnt

                        
            
def bingo():
    for i in range(5):
        mc = input().split()
        for j in range(5):
            visit_bingo(mc[j])
            check_bingo(visited)
                
            if cnt_bingo() >= 3 :
                return i*5+j+1  

print(bingo())
