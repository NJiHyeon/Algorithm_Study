def solution(places):
    dr = [0, 1, 0, -1]
    dc = [1, 0, -1, 0]

    def dfs(cur_r, cur_c, curr_n):
        # 탈출 조건
        if curr_n >= 2:
            return
        # 반복 수행
        for i in range(4):
            next_r = cur_r + dr[i]
            next_c = cur_c + dc[i]
            if 0 <= next_r < 5 and 0 <= next_c < 5:
                if not visited[next_r][next_c]:
                    if place[next_r][next_c] == 'P':
                        return False
                    elif place[next_r][next_c] == 'O':
                        visited[next_r][next_c] = True
                        if dfs(next_r, next_c, curr_n+1) == False:
                            return False
                        visited[next_r][next_c] = False
        return True


    answer = []
    for p in range(5):
        place = places[p]
        result = 1
        visited = [[False]*5 for _ in range(5)]
        for r in range(5):
            for c in range(5):
                if place[r][c] == "P":
                    visited[r][c] = True
                    if not dfs(r, c, 0):
                        result = 0
                    visited[r][c] = False
        answer.append(result)

    return answer