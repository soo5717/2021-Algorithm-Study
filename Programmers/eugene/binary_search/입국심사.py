def solution(n, times):  
    left=n*min(times)//len(times)
    right=n*max(times)//len(times)
    
    while(left<=right):
        people=0
        mid=(left+right)//2 
        for i in times:
            people+=mid//i

        if people >= n:
            right=mid-1
        else:
            left=mid+1
    return right