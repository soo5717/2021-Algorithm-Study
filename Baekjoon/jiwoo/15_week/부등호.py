num = int(input())
operator = input().split()

visited = [0] * 10
max_num = ""
min_num = ""

def check_oper(a, b, o):
    if o == '<':
        return a<b
    else:
        return a>b

def solve(count, num_str):
    global max_num, min_num
    if count == num+1:
        if not min_num:
            min_num = num_str
        else:
            max_num = num_str
        return
    for i in range(10):
        if not visited[i]:
            if count == 0 or check_oper(num_str[-1], str(i), operator[count-1]):
                visited[i] = True
                solve(count+1, num_str+str(i))
                visited[i] = False
                
solve(0, "")
print(max_num)
print(min_num)