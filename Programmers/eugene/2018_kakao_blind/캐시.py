def solution(cacheSize, cities):
    answer = 0
    my_cache=[]
        
    if cacheSize ==0:
        return len(cities)*5
    
    for city in cities:
        city=city.lower()
        if city in my_cache: #my_cache에 city가 있으면
            answer+=1
            my_cache.remove(city)
        else: #없으면
            answer+=5
            if len(my_cache)==cacheSize:
                del my_cache[0] #cache가 꽉 차있으면 맨 앞을 비우기
        my_cache.append(city) #city추가.
    return answer
