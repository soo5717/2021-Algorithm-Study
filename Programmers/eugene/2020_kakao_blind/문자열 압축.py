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

            if(cnt==1):
                result+=str(first)
            else:
                result+= str(cnt)+str(first)
                
        answer+=[len(result)]
    return 1 if answer==[] else min(answer)
