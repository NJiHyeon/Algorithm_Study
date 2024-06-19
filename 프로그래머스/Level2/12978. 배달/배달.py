def solution(N, road, K):
    import heapq
    answer = 0
    graph = {}
    INF = int(1e9) # 무한을 의미하는 값으로 10억을 설정
    distance = [INF] * (N+1)
    
    # graph 만들기
    for i in road:
        if i[0] in graph:
            graph[i[0]].append((i[1], i[2]))
        else:
            graph[i[0]] = [(i[1], i[2])]
            
        if i[1] in graph:
            graph[i[1]].append((i[0], i[2]))
        else:
            graph[i[1]] = [(i[0], i[2])]

    # heapq
    q = []
    heapq.heappush(q, (0, 1)) #(거리, 노드)
    distance[1] = 0
    while q:
        dist, node = heapq.heappop(q)
        # 0번 노드에서 node번 노드까지 현재 저장되어 있는 거리가 더 짧은 경우는 이게 최소이므로 갱신할 필요 없으니까 무시
        if distance[node] < dist:
            continue
        # 0번 노드에서 node번 노드까지 거리가 q에 저장되어 있는게 더 짧은 경우, 해당 node와 연결된 node들의 거리를 다시 확인

        for i in graph[node]:
            cost = dist + i[1]
            if cost < distance[i[0]]:
                distance[i[0]] = cost
                heapq.heappush(q, (cost, i[0]))
    distance = distance[1:]
    for d in distance:
        if d <= K:
            answer += 1
    return answer