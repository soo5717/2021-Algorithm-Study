from math import ceil,log
import sys

MOD = 1000000007

def init(start, end, node):
    if start==end:
        tree[node]=arr[start]
        return tree[node] % MOD
    mid= (start+end)//2
    tree[node]=init(start, mid, node*2) * init(mid+1, end, node*2+1) % MOD
    return tree[node]

def update(start, end, node, idx, num):
    if idx < start or end < idx: return
    if start == end:
        tree[node]=num
        return
    
    mid=(start+end)//2
    update(start, mid, node*2, idx, num)
    update(mid+1, end, node*2+1, idx, num)
    tree[node]=(tree[node*2]*tree[node*2+1]) % MOD
    return tree[node]

def query(start, end, node, left, right):
    if right < start or end < left: return 1
    if left <=start and end <= right: return tree[node] % MOD
    
    mid=(start+end)//2
    return query(start,mid, node*2, left, right)*query(mid+1, end, node*2+1, left, right) % MOD

if __name__ =="__main__":
    N,M,K=map(int, input().split())
    size=2**(ceil(log(N,2))+1)
    tree=[1]*size
    arr=[]
    for i in range(N):
        arr.append(int(sys.stdin.readline()))
    
    init(0,N-1,1)

    for _ in range(M+K):
        a,b,c=map(int, sys.stdin.readline().split())
        if a==1:
            update(0, N-1, 1, b-1, c)
        elif a==2:
            print(query(0, N-1, 1, b-1, c-1))
