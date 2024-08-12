def solution(n, paths, gates, summits):
    import heapq
    #🧊 가중치 그래프 만들기
    summits.sort()
    summit_set = set(summits)
    
    graph = {}
    for path in paths:
        a, b, c = path[0], path[1], path[2]
        if a in graph:
            graph[a].append([b, c])
        else:
            graph[a] = [[b, c]]
        
        if b in graph:
            graph[b].append([a, c])
        else:
            graph[b] = [[a, c]]
    pq = []
    visited = [10000001] * (n+1)
    
    #🧊 모든 출입구를 우선순위 큐에 삽입한다. 
    for gate in gates:
        heapq.heappush(pq, (0, gate))
        visited[gate] = 0
    
    #🧊 intensity를 기준으로 다익스트라를 진행한다. 
    while pq:
        intensity, node = heapq.heappop(pq)
        if intensity > visited[node] or node in summit_set:
            continue 
        
        for next_node, weight in graph[node]:
            # 하나의 길 과정에서는 최댓값 구함
            next_intensity = max(weight, intensity)
            # 단, 각 등산로랑 비교할때는 최소값 저장
            if next_intensity < visited[next_node]:
                visited[next_node] = next_intensity
                heapq.heappush(pq, (next_intensity, next_node))
            
    #🧊 다익스트라 완료 후 산봉우리들을 순회하며 정답을 찾는다. 
    # (순서대로 정렬되어 있으므로 같을 떄는 생각 안해도 된다.)
    min_intensity = [0, 10000001]
    for summit in summits:
        if min_intensity[1] > visited[summit]:
            min_intensity[0] = summit
            min_intensity[1] = visited[summit]
    return min_intensity