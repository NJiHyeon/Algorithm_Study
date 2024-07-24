def solution(places):
    from collections import deque
    def inRange(r, c):
        return 0 <= r < 5 and 0 <= c < 5
    
    def bfs(i, j, place):
        dr = [0, -1, 0, 1]
        dc = [1, 0, -1, 0]
        queue = deque()
        queue.append((i, j, 0))
        visited = [[False]*5 for _ in range(5)]
        visited[i][j] = True
        while queue:
            cur_r, cur_c, cur_dist = queue.popleft()
            for i in range(4):
                next_r = cur_r + dr[i]
                next_c = cur_c + dc[i]
                next_dist = cur_dist + 1
                if inRange(next_r, next_c) and place[next_r][next_c] != 'X' and not visited[next_r][next_c]:
                    if next_dist > 2:
                        continue
                    elif place[next_r][next_c] == 'P':
                        return False
                    else:
                        queue.append((next_r, next_c, next_dist))
                        visited[next_r][next_c] = True
        return True
            
    answer = []
    for place in places:
        result = 0
        p = 0
        for i in range(5):
            for j in range(5):
                if place[i][j] == 'P':
                    p += 1
                    result += bfs(i, j, place)
        if result == p:
            answer.append(1)
        else:
            answer.append(0)
    return answer