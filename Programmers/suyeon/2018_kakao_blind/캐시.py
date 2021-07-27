from collections import deque

def solution(cacheSize, cities):
    if not cacheSize: 
        return len(cities) * 5
    
    answer = 0
    cache = deque(maxlen = cacheSize)
    for city in cities:
        city = city.lower()
        if city in cache:
            cache.remove(city)
            cache.append(city)
            answer += 1
        else:
            cache.append(city)
            answer += 5
    return answer