def solution(cacheSize, cities):
    
    cache = []
    answer = 0
    if cacheSize == 0 :
        return len(cities) * 5
    for city in cities :
        city = city.lower()
        if city not in cache :
            if len(cache) >= cacheSize :
                cache.pop(0)
            cache.append(city)
            answer += 5
        else : 
            cache.remove(city)
            cache.append(city)
            answer += 1
    return answer