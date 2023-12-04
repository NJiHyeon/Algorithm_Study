def solution(scoville, K) :
    import heapq
    heapq.heapify(scoville)
    n = 0
    s = heapq.heappop(scoville)
    heapq.heappush(scoville, s)
    if s >= K :
        return 0
    
    while len(scoville)>1 :
        first = heapq.heappop(scoville) 
        second = heapq.heappop(scoville)
        mix = first + 2*second
        heapq.heappush(scoville, mix)
        n += 1
        result = heapq.heappop(scoville) 
        if result >= K :
            return n
        else :
            heapq.heappush(scoville, result)
        
    return -1