from collections import deque 

N, M = map(int, input().split())
r, c, d = map(int, input().split())

graph = []
visit = [[False for _ in range(M)] for _ in range(N)]
for _ in range(N):
    graph.append(list(map(int, input().split())))


forw_dr = [-1, 0, 1, 0]
forw_dc = [0, 1, 0, -1]
back_dr = [1, 0, -1, 0] 
back_dc = [0, -1, 0, 1]

def robot(r, c, d):
    clean_room = 0
    while True:
        # 1. 현재 칸 청소 여부
        if graph[r][c] == 0 and visit[r][c] == False:
            clean_room += 1
            visit[r][c] = True

        # 2. 주변 칸 청소 여부
        clean = True
        for i in range(4):
            next_r = r + forw_dr[i]
            next_c = c + forw_dc[i]
            if 0 <= next_r < N and 0 <= next_c < M :
                if graph[next_r][next_c] == 0:
                    if visit[next_r][next_c] == False:
                        clean = False 
                        break
        if clean == True:
            # 방향 유지한 채로 후진 
            r = r + back_dr[d]
            c = c + back_dc[d]
            if 0 <= r < N and 0 <= c < M:
                if graph[r][c] == 1:
                    return clean_room
        else:
            # 90도 회전
            while True:
                d -= 1
                if d < 0:
                    d = 3
                next_r = r + forw_dr[d]
                next_c = c + forw_dc[d]
                if 0 <= next_r < N and 0 <= next_c < M :
                    if graph[next_r][next_c] == 0:
                        if visit[next_r][next_c] == False:
                            r += forw_dr[d]
                            c += forw_dc[d]
                            break

print(robot(r, c, d))