from collections import defaultdict

def solution(n, results):
    win_results, loses_results = defaultdict(set), defaultdict(set)
    
    for a, b in results:
        win_results[a].add(b)
        loses_results[b].add(a)
    
    for i in range(1, n + 1):
        for loser in win_results[i]:
            loses_results[loser].update(loses_results[i])
        for winner in loses_results[i]:
            win_results[winner].update(win_results[i])
    
    answer = 0
    for i in range(1, n + 1):
        if len(win_results[i]) + len(loses_results[i]) == n -1:
            answer += 1
    return answer