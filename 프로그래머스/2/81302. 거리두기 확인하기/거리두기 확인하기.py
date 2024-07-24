def solution(places):
    from collections import deque
    def in_Range(r, c):
        return 0 <= r < 5 and 0 <= c < 5
    
    # bfs code
    def bfs(r, c, place):
        dr = [0, 1, 0, -1]
        dc = [1, 0, -1, 0]
        q = deque()
        q.append((r, c, 0))
        visited = [[False]*5 for _ in range(5)]
        visited[r][c] = True
        while q:
            cur_r, cur_c, cur_dist = q.popleft()
            for i in range(4):
                next_r = cur_r + dr[i]
                next_c = cur_c + dc[i]
                next_dist = cur_dist + 1
                if in_Range(next_r, next_c) and not visited[next_r][next_c] and place[next_r][next_c] != 'X':
                    if next_dist > 2:
                        continue
                    elif place[next_r][next_c] == 'P':
                        return False
                    else:
                        q.append((next_r, next_c, next_dist))
                        visited[next_r][next_c] = True
        return True
                
    
    # one place code
    def one_place(place):
        for r in range(5):
            for c in range(5):
                if place[r][c] == 'P':
                    if not bfs(r, c, place):
                        return False
        return True
    
    
    # main code
    answer = []
    for place in places:
        if one_place(place):
            answer.append(1)
        else:
            answer.append(0)
    return answer
    