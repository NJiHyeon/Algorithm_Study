
import sys
sys.setrecursionlimit(int(1e7))

def dfs(maps, i, j, n, m, visit):
    visit[i][j] = True
    area = int(maps[i][j])
    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]

    for dx, dy in directions:
        x, y = i + dx, j + dy
        if 0 <= x < n and 0 <= y < m and not visit[x][y] and maps[x][y] != 'X':
            area += dfs(maps, x, y, n, m, visit)

    return area

def solution(maps):
    answer = []
    n, m = len(maps), len(maps[0])
    visit = [[False] * m for _ in range(n)]

    for i in range(n):
        for j in range(m):
            if maps[i][j] != 'X' and not visit[i][j]:
                answer.append(dfs(maps, i, j, n, m, visit))

    if answer:
        return sorted(answer)
    else:
        return [-1]