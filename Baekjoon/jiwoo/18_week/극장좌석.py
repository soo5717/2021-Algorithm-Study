N = int(input())
M = int(input())

vip = []
for i in range(M):
	vip_n = int(input())
	vip.append(vip_n)

sit = [1, 1, 2]
for i in range(3, N+1):
	sit.append(sit[i-2] + sit[i-1])

answer = 1
if M >= 1:
	start_num = 0
	for i in range(M):
		answer *= sit[vip[i]-1-start_num]
		start_num = vip[i]
	answer *= sit[N-start_num]
else:
	answer = sit[N]
print(answer)