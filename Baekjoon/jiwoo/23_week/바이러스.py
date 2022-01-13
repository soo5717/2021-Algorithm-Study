def dfs(com):
    global count
    visited[com] = 1
    for i in connection[com]:
        if visited[i] == 0:
            dfs(i)
            count += 1

com_num = int(input())
net_com = int(input())

count = 0
visited = [0] * (com_num + 1)

connection = [[] * com_num for _ in range(com_num + 1)]
for _ in range(net_com):
    a, b = map(int, input().split())
    connection[a].append(b)
    connection[b].append(a)
   
dfs(1)
print(count)