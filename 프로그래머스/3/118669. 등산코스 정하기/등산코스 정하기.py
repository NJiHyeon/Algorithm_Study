def solution(n, paths, gates, summits):
    # summits 돌고 gates 안에 있는 노드가 나오면 return 
    # pop : 작은거부터
    # next 값 : max(현재 노드의 값, 연결된 선의 값)
    # next 노드 : 저장된 값보다 작으면 작은 값으로 바꾸기 (이 길로 올 수 있다는 거니까)
    import heapq
    graph = {i : [] for i in range(1, n+1)}
    for u in range(len(paths)):
        i, j, w = paths[u][0], paths[u][1], paths[u][2]
        graph[i].append((j, w))
        graph[j].append((i, w))
        
    def dijkstra(graph, start_v, n):
        times = [float("inf")] * (n+1)
        times[start_v] = 0
        pq = [(0, start_v)]
        
        while pq:
            cur_time, cur_v = heapq.heappop(pq)
            #저장된 값이 이미 더 작으면 볼 필요 없음.
            if cur_v in gates:
                return cur_time
            if times[cur_v] < cur_time or (cur_v != start_v and cur_v in summit_set): 
                continue
                
            for next_v, time in graph[cur_v]:
                next_time = max(times[cur_v], time)
                if times[next_v] > next_time :
                    times[next_v] = next_time
                    heapq.heappush(pq, (next_time, next_v))
        return 10000001

    result = []
    summit_set = set(summits)
    for summit in summits:
        o = dijkstra(graph, summit, n)
        heapq.heappush(result, (o, summit))
    min_time, summit = heapq.heappop(result)
    return [summit, min_time]
        
        
        
        
        
        
        