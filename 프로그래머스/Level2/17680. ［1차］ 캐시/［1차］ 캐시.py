def solution(cacheSize, cities):
    answer = 0
    cache = []
    if cacheSize == 0 :
        answer = 5*len(cities)
    else :
        for city in cities :
            city=city.lower()
            if len(cache) < cacheSize :
                if city in cache :
                    answer += 1
                    cache.pop(cache.index(city))
                    cache.append(city)
                else :
                    answer += 5
                    cache.append(city)
            else :
                if city in cache :
                    answer += 1
                    cache.pop(cache.index(city))
                    cache.append(city)
                else :
                    answer += 5
                    cache.pop(0)
                    cache.append(city)
            
    return answer