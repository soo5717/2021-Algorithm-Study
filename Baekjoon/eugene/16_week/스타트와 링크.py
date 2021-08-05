from itertools import combinations
import sys

def solution(potential, n):
    minimum = 10000
    StartLink = set(range(n))
    for startTeam in combinations(range(n),n//2):
        sum1,sum2 = 0,0
        startTeam=set(startTeam)
        linkTeam = StartLink-startTeam

        for a in startTeam:
            for b in startTeam:
                sum1 += potential[a][b]

        for a in linkTeam:
            for b in linkTeam:
                sum2 += potential[a][b]

        ans = sum1-sum2 if sum1>=sum2 else sum2-sum1
        
        if ans == 0: return 0
        if ans < minimum: minimum = ans
            
    return minimum

if __name__ == "__main__":
    potential = []
    N = int(input())

    for _ in range(N):
        potential.append(list(map(int, sys.stdin.readline().split())))
    print(solution(potential, N))
