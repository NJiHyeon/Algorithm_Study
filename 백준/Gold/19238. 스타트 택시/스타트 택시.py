import sys
from collections import deque 

# 입력 형식에 맞춰서 입력값을 받는다.
input = sys.stdin.readline
N, M, fuel = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(N)]
tr, tc = map(int, input().split())
tr -= 1
tc -= 1
answer = 0

# 승객 정보 만들기 : 승객의 출발지와 도착지를 해시테이블로 저장
passenger = {}
for _ in range(M):
    pr, pc, pdr, pdc = map(int, input().split())
    passenger[(pr-1, pc-1)] = (pdr-1, pdc-1)

# 필요한 함수 정의
def in_range(next_r, next_c):
    return 0 <= next_r < N and 0 <= next_c < N


def pickup(tr, tc):
    queue = deque()
    visited = set()
    queue.append([tr, tc, 0])
    visited.add((tr, tc))
    candidate = []
    min_distance = 1000000
    while queue:
        cur_r, cur_c, cur_d = queue.popleft()
        if cur_d > min_distance:
            break
        if (cur_r, cur_c) in passenger:
            candidate.append((cur_r, cur_c))
            min_distance = cur_d
        for dr, dc in [[-1, 0], [1, 0], [0, -1], [0, 1]]:
            next_r, next_c, next_d = cur_r+dr, cur_c+dc, cur_d+1
            if (next_r, next_c) in visited:
                continue
            if 0 <= next_r < N and 0 <= next_c < N and board[next_r][next_c] != 1:
                queue.append([next_r, next_c, next_d])
                visited.add((next_r, next_c))

    return candidate, min_distance


def go_dest(tr, tc):
    pdr, pdc = passenger[(tr, tc)]
    del passenger[(tr, tc)]
    queue = deque()
    queue.append([tr, tc, 0])
    visited = set()
    visited.add((tr, tc))
    while queue:
        cur_r, cur_c, cur_d = queue.popleft()
        if cur_r == pdr and cur_c == pdc:
            return cur_r, cur_c, cur_d
        for dr, dc in [[-1,0],[1,0],[0,-1],[0,1]]:
            next_r, next_c, next_d = cur_r+dr, cur_c+dc, cur_d+1
            if (next_r, next_c) in visited:
                continue
            if in_range(next_r, next_c) and board[next_r][next_c] != 1:
                queue.append([next_r, next_c, next_d])
                visited.add((next_r, next_c))
    return pdr, pdc, 1000000


# 남아 있는 승객이 있다면 계속 실행
while len(passenger) != 0:
		#⭐ 1. BFS 알고리즘으로 현재 택시 위치로부터 승객까지의 최단거리 계산 -> pickup, 연료/승객 확인
    cand, used_fuel = pickup(tr, tc)
    if used_fuel > fuel:
        answer = -1
        break
    fuel -= used_fuel
    #⭐ 2. 최단거리 기준으로 가장 높은 우선순위의 승객 위치로 택시 이동
    tr, tc = sorted(cand)[0]
		#⭐ 3. 다시 BFS 알고리즘을 통해 승객을 도착지까지 이동시키고 연료 보충 -> go_dest
    pdr, pdc, used_fuel = go_dest(tr, tc)
    if used_fuel > fuel:
        answer = -1
        break 
    fuel -= used_fuel
    fuel += 2*used_fuel
    tr, tc = pdr, pdc 

# 이동 성공 여부에 따라 출력값 결정
	# 모든 승객 이동시키기에 성공한다면 남은 연료 출력
	# 승객 이동시키기에 실패한다면 -1 출력
if answer == -1:
    print(-1)
else:
    print(fuel)