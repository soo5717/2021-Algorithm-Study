def check_index(a, n):
	for i in range(n):
		index_.append(a[1].index(a[0][i]))

def print_key(a, b):
	for i in b:
		print(a[2][i], end=' ')

T = int(input())

for i in range(T):
	n = int(input())
	
	input_ = []
	for j in range(3):
		input_.append(input().split())
		
	index_ = []
	check_index(input_, n)

	print_key(input_, index_)