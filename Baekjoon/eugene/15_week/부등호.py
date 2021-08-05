num=int(input())
oper=input().split()
visited=[False]*(10)
max_num, min_num="",""

def check_num(i,j,oper):
    return i<j if oper=='<' else i>j

def solution(cnt,ansList):
    global max_num, min_num

    if cnt == num+1:
        if not min_num : min_num=ansList
        else: max_num=ansList
        return

    for i in range(10):
        if not visited[i]:
            if cnt == 0 or check_num(ansList[-1], str(i), oper[cnt-1]):
                visited[i]=True
                solution(cnt+1, ansList+str(i))
                visited[i]=False

solution(0,"")
print(max_num)
print(min_num)
