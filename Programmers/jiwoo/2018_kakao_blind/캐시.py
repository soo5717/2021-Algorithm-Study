from collections import deque

def solution(cacheSize, cities):
    times = 0
    buffer = deque()
    
    if cacheSize == 0:
        return len(cities)*5
    else:
        for city in cities:
            city = city.upper()
            if city in buffer:
                times += 1
                buffer.remove(city)
            else:
                times += 5
                if len(buffer) >= cacheSize:
                    buffer.popleft()
            buffer.append(city)
    return times