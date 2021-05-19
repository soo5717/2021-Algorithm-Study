def solution(N, number):
    if(N==number):
        return 1
    temp=[[N]]
    for i in range(1,8):
        temp.append([])
        cnt=i+1
        #[cnt-k,k]를 돌면서 모든 경우를 구한다.
        temp[i].append(int(str(N)*cnt))

        #[cnt-1,1] [cnt-2,2] [cnt-k, y=k]
        for k in range(1,cnt//2+1): 
            for x in temp[cnt-k-1]:
                for y in temp[k-1]:
                    temp[i].append(x+y)
                    temp[i].append(x-y) 
                    temp[i].append(y-x) 
                    temp[i].append(x*y)    
                    temp[i].append(x//y)
        temp[i]=list(set(temp[i])) #중복, 0제거
        if 0 in temp[i]:
            temp[i].remove(0)   
        if number in temp[i]:
            return cnt
    return -1
