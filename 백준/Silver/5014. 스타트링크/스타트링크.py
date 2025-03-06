from collections import deque 

F, S, G, U, D = map(int, input().split())
visit = [False] * (1000001)

def bfs():
    q = deque()
    q.append((S, 0))
    visit[S] = True 

    while q:
        cur_s, cur_n = q.popleft()
        if cur_s == G:
            return cur_n
        for s in [U, -D]:
            next_s = cur_s + s
            if 1 <= next_s <= F:
                if visit[next_s] == False:
                    visit[next_s] = True 
                    q.append((next_s, cur_n+1))

    return "use the stairs"


print(bfs())