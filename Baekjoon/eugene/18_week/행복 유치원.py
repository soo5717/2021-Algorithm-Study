if __name__ =="__main__":
    n,k = map(int, input().split())
    people = list(map(int, input().split()))

    diff=[0]*(n-1)
    for i in range(n-1):
        diff[i] = people[i+1]-people[i]
    diff.sort()
    print(sum(diff[:n-k]))
