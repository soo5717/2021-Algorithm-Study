from collections import deque

def dfs(begin, target, words, visited):
    answer = 0
    
    queue = deque([begin])
    while queue:
        begin = queue.pop()
        if begin == target: 
            break
        
        for i, word in enumerate(words):
            if len([j for j in range(len(word)) if begin[j] != word[j]]) == 1:
                if not visited[i]:
                    # print(word)
                    queue.append(word)
                    visited[i] = True
        print(queue)
        answer += 1
    
    if begin != target: 
        return 0
    
    return answer
    
def solution(begin, target, words):
    # 단어가 없는 경우
    if target not in words: return 0
    
    return dfs(begin, target, words, [False] * len(words))