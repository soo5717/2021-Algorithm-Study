def solution(n, results):
    count = 0
    winners, losers = {}, {}
    
    for i in range(1, n+1):
        winners[i], losers[i] = set(), set()
        
    for i in range(1, n+1):
        for result in results:
            if result[0] == i:
                winners[i].add(result[1])
            if result[1] == i:
                losers[i].add(result[0])
                
        for winner in losers[i]:
            winners[winner].update(winners[i])
        for loser in winners[i]:
            losers[loser].update(losers[i])
    
    for i in range(1, n+1):
        if len(winners[i]) + len(losers[i]) == n-1:
            count += 1
    return count