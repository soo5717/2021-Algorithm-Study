# backtracking
MIN_NUM = '9999999999'
MAX_NUM = '0'

def backtracking(first, idx, answer, numbers, inequalities):
  if(idx == len(inequalities)):
    global MIN_NUM, MAX_NUM
    answer_int = int(answer+str(first))
    if answer_int < int(MIN_NUM): MIN_NUM = answer+str(first)
    if answer_int > int(MAX_NUM): MAX_NUM = answer+str(first)
    return

  numbers[first] = True
  for second in range(10):
    if not numbers[second]:
      if inequalities[idx] == '<' and first < second:
        backtracking(second, idx + 1, answer + str(first), numbers, inequalities)
      if inequalities[idx] == '>' and first > second:
        backtracking(second, idx + 1, answer + str(first), numbers, inequalities)
  numbers[first] = False

k = input()
inequalities = list(map(str, input().split()))
numbers = [False] * 10 # 0 ~ 9

for i in range(10):
  backtracking(i, 0, '', numbers, inequalities)

print(MAX_NUM)
print(MIN_NUM)