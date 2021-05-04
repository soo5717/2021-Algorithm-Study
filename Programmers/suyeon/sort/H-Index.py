def solution(citations):
    citations.sort()
    
    n = len(citations)
    for i, citation in enumerate(citations):
        if citation >= n - i:
            return n - i
    return 0