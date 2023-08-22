# 미로탈출칸 만들기
n, m = map(int, input().split())
miro = []
for i in range(n) :
    miro.append(list(map(int, input())))
    
# 이동할 네가지 방향 정의 (상,하,좌,우)
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

# BFS 소스코드 구현
from collections import deque
def bfs(x, y) :
    # 큐 (Queue) 구현을 위해 deque 라이브러리 사용
    queue = deque()
    queue.append((x, y))
    # 큐가 빌 대까지 반복
    while queue :
        x, y = queue.popleft() # (0, 0)
        # 현재 위치에서 4가지 방향으로 위치 확인
        for i in range(4) :
            nx = x + dx[i]
            ny = y + dy[i]
            # 미로 찾기 공간을 벗어난 경우 무시
            if nx<0 or nx>=n or ny<0 or ny>=m :
                continue
            # 벽인 경우 무시
            if miro[nx][ny] == 0 :
                continue
            # 해당 노드를 처음 방문하는 경우에만 최단 거리 기록
            if miro[nx][ny] == 1 :
                miro[nx][ny] = miro[x][y] + 1
                queue.append((nx, ny)) # 중요 (위치를 큐에 넣고 빼서 더하고 넣고 빼고 반복)
    # 가장 오른쪽 아래까지의 최단 거리 반환
    return miro[n-1][m-1]

print(bfs(0, 0))