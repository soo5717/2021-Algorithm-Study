import sys

if __name__ =="__main__":
    n = int(input())
    m = int(input())

    x, y = 1,2
    fibo = [1] * (n+1)
    for i in range(2,n+1):
        fibo[i] = fibo[i-1]+fibo[i-2]
    idx, answer = 1,1
    for _ in range(m):
        x = int(sys.stdin.readline())
        answer *= fibo[x-idx]
        idx = x+1
        
    if idx < n :
        answer *= fibo[n-idx+1]
    print(answer)
