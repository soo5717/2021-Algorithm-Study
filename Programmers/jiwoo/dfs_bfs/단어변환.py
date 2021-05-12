def solution(begin, target, words):
    answer = [begin]

    if target not in words:
        return 0
    
    levelCount = 0
    while len(words):
        for beginWord in answer:
            change = []
            for word in words:
                count = 0
                for i in range(len(beginWord)):
                    if beginWord[i] != word[i]:
                        count += 1
                    if count == 2:
                        break
                if count == 1:
                    change.append(word)
                    words.remove(word)
        levelCount += 1
        if target in change:
            return levelCount
        else:
            answer = change
    return 0