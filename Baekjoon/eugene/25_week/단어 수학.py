n = int(input())

num_list = {i: [] for i in range(10)}
alphabet_num = {}

for _ in range(n):
    word = list(input())
    for idx, value in enumerate(word):
        alphabet_num[value] = 0
        num_list[len(word) - idx] += {value}

for key in range(9, -1, -1):
    for num in (num_list[key]):
        alphabet_num[num] += 10**(key-1)

sorted_alphabet = sorted(alphabet_num.items(), key = lambda item: item[1], reverse=True)

answer = 0
for idx, (_, operand) in enumerate(sorted_alphabet):
    answer += operand * (9-idx)
print(answer)
