import sys

input = sys.stdin.readline
N = int(input())

word_list = []
alpha_count_list = {}
sum_list = []

for i in range(N):
    word_list.append(input().rstrip())

for i in range(N):
    for j in range(len(word_list[i])):
        if word_list[i][j] in alpha_count_list:
            alpha_count_list[word_list[i][j]] += 10 ** (len(word_list[i]) - j - 1)
        else:
            alpha_count_list[word_list[i][j]] = 10 ** (len(word_list[i]) - j - 1)

for num in alpha_count_list.values():
    sum_list.append(num)

sum_list.sort(reverse = True)

sum = 0
cal_num = 9
for i in sum_list:
    sum += cal_num * i
    cal_num -= 1

print(sum)
