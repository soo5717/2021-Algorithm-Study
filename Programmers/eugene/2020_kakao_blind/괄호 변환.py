def solution(p):
    if not p: return "" #step1
    
    u,v,proper = divide_correct(p) #step2+3
    
    if proper : #step3 
        return u+solution(v)
    
    else : #step4
        result='('
        result +=solution(v)
        result+=')'
        
        reverse=''.join([')' if i=='(' else '(' for i in u[1:len(u)-1] ])
        result+=reverse
        return result
        
        
def divide_correct(s): #u,v 분리+올바른 괄호 판별
    left,right=0,0
    proper=True
    
    for i in range(len(s)):
        if s[i]=="(": left+=1
        else: right+=1
            
        if left < right:#한번이라도 right가 크면 올바르지 않은 문자열
            proper=False    
        if(left==right): #균형잡힌 괄호 문자열 u,v 분리
            u= s[:i+1]
            v= s[i+1:]
            return u,v,proper
