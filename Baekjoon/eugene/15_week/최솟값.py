from math import ceil, log
import sys

def init(start, end, node):
    if start==end:
        tree[node]=tree[size+start]
        return tree[node]
     
    mid=(start+end)//2
    tree[node]=min(init(start,mid,node*2), init(mid+1, end, node*2+1))
    return tree[node]

def query(start, end, node, q_start, q_end):
    if start > q_end or end < q_start:
        return 1000000000
    elif q_start<=start and end <= q_end:
        return tree[node]
    mid=(start+end)//2
    return min(query(start, mid, node*2, q_start, q_end),query(mid+1,end, node*2+1, q_start, q_end))
    
    
if __name__ =="__main__":
    N,M=[int(x) for x in sys.stdin.readline().split()]
    size =2**(ceil(log(N,2))+1)
    tree_size=2*size
    tree=[0]*tree_size
    
    for i in range(N):
        tree[size+i]=int(sys.stdin.readline())

    init(0,N-1,1)
    
    for _ in range(M):
        q_start, q_end= map(int, sys.stdin.readline().split())
        print(query(0,N-1,1,q_start-1, q_end-1))
