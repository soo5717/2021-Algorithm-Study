def solution(distance, rocks, n):
    left, right=0, distance
    
    rocks.sort()
    rocks.append(distance)
    
    while(left<=right):
        brk_rocks, stay_rock = 0,0
        mid=(left+right)//2
        for rock in rocks:
            if (rock - stay_rock >= mid):
                stay_rock = rock
            else :
                brk_rocks +=1

        if brk_rocks > n:
            right=mid-1
        else:
            left=mid+1    
    return right