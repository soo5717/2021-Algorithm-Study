def solution(begin, target, words):
    answer = 0
    stack = [begin]

    while True:
        temp = []
        for word in stack:
            if word == target: return answer
            
            for i in range(len(words)-1, -1, -1): # Index Error 방지
                if sum([x!=y for x, y in zip(word, words[i])]) == 1:
                    temp.append(words.pop(i))
        # print(temp)
        if not temp: return 0
        stack = temp
        answer += 1