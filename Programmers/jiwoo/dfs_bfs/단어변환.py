def solution(begin, target, words):
    answer = 0
    queue = [begin]
    while True:
        temp = []
        for word in queue:
            if word == target:
                return answer
            for index in range(len(words)-1, -1, -1):
                word2 = words[index]
                difference = sum([x != y for x, y in zip(word, word2)])
                if difference == 1:
                    temp.append(words.pop(index))
        if not temp:
            return 0
        queue = temp
        answer += 1