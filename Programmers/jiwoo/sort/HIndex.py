def solution(citations):
    citations.sort(reverse=True)
    h = len(citations)
    
    while True:
        count = 0
        for c in citations:
            if c >= h:
                count += 1
            if count >= h:
                return h
        h -= 1