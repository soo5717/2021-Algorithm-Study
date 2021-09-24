def solution(n):
    if n == 1:
        return 1
    
    ans = [1] * n
    ans[1] =3
    
    for i in range(2,n):
        ans[i]=(ans[i-1] + ans[i-2]*2)%10007
    return ans[-1]

if __name__ =="__main__":
    n=int(input())
    print(solution(n))
