from collections import deque 

N, M = map(int, input().split())

visit = [False for _ in range(100001)]

def bfs():
    q = deque()
    q.append((N, 0))
    visit[N] = True

    while q:
        cur_v, cur_n = q.popleft()
        if cur_v == M:
            return cur_n
        
        for next_v in [cur_v+1, cur_v-1, 2*cur_v]:
            if 0 <= next_v <= 100000 and visit[next_v] == False:
                q.append((next_v, cur_n + 1))
                visit[next_v] = True 

print(bfs())