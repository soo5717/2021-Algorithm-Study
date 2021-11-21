import sys
from collections import defaultdict

input = sys.stdin.readline

words = []
alphabet_dict = {}
alphabet_sum_dict = defaultdict(int)

N = int(input())
for _ in range(N):
    word = input().strip()
    words.append(word)

    word_length = len(word)
    for index, alphabet in enumerate(word):
        alphabet_sum_dict[alphabet] += pow(10, word_length - index - 1)

sum_number = 0
remain_number = 9
for key, value in sorted(alphabet_sum_dict.items(), reverse=True, key=lambda item: item[1]):
    sum_number += value * remain_number
    remain_number -= 1

print(sum_number)
