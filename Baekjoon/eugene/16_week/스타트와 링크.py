from itertools import combinations
import sys

def solution(potential, n):
    minimum = 10000
    StartLink = set(range(n))
    for startTeam in combinations(range(n),n//2):
        sum1,sum2 = 0,0
        startTeam=list(startTeam)
        linkTeam = list(StartLink-set(startTeam))

        for a in range(n//2):
            for b in range(a+1,n//2):
                Sx, Sy = startTeam[a], startTeam[b]
                sum1 += potential[Sx][Sy]+potential[Sy][Sx]

                Lx, Ly = linkTeam[a], linkTeam[b]
                sum2 += potential[Lx][Ly]+potential[Ly][Lx]
        ans=abs(sum1-sum2)
        
        if not ans : return 0
        if ans < minimum: minimum = ans
            
    return minimum

if __name__ == "__main__":
    potential = []
    N = int(input())

    for _ in range(N):
        potential.append(list(map(int, sys.stdin.readline().split())))
    print(solution(potential, N))
