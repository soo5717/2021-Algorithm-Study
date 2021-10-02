bingo = [list(map(int, input().split())) for _ in range(5)]

numbers = []
for _ in range(5):
	numbers += list(map(int, input().split()))

counting = [0] * 12

bingo_line = 0
flag = False
for n in range(0, 26):
	if flag == True:
		break
	for i in range(5):
		if flag == True:
			break
		for j in range(5):
			if flag == True:
				break
			if numbers[n] == bingo[i][j]:
				bingo[i][j] = 0
				counting[i] += 1
				counting[j+5] += 1
				if i == j:
					counting[10] += 1
				if i+j == 4:
					counting[11] += 1
				for count in range(12):
					if counting[count] == 5:
						counting[count] = 0
						bingo_line += 1
						if bingo_line == 3:
							flag = True
							break
print(n)