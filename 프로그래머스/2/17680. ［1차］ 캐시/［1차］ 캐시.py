def solution(cacheSize, cities):
    from collections import deque 
    
    answer = 0
    cache_list = deque()
    
    if cacheSize == 0:
        return 5 * len(cities)
    
    for city in cities:
        city = city.lower()
        if city in cache_list:
            # i = cities.index(city)
            cache_list.remove(city)
            cache_list.append(city)
            answer += 1
        else:
            if len(cache_list) < cacheSize:
                cache_list.append(city)
            else:
                cache_list.popleft()
                cache_list.append(city)
            answer += 5
    return answer