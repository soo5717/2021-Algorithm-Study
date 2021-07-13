def solution(s):
    answer=[]
    for i in range(1, len(s)//2+1):
        result = ""
        word=s
        while word:
            first=word[:i]
            word=word[i:]
            cnt=1
            while (first==word[:i]):
                cnt+=1
                word=word[i:]
            result += str(first) if cnt== 1 else str(cnt)+str(first)   
        answer+=[len(result)]
    return 1 if answer==[] else min(answer)
