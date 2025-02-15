def solution(places):
    from collections import deque

    def dfs(r, c, n, place, visit):
        dr = [0, 1, 0, -1]
        dc = [1, 0, -1, 0]

        visit[(r, c)] = True 
        for i in range(4):
            next_r = r + dr[i]
            next_c = c + dc[i]
            if 0 <= next_r < 5 and 0 <= next_c < 5:
                if (next_r, next_c) not in visit:
                    if place[next_r][next_c] == 'P':
                        return 0
                    elif place[next_r][next_c] == 'O' and n == 0:
                        if dfs(next_r, next_c, n+1, place, visit) == 0:
                            return 0
        return 1


    def main(place):
        visit = {}
        for r in range(5):
            for c in range(5):
                if place[r][c] == 'P' and (r, c) not in visit:
                    if dfs(r, c, 0, place, visit) == 0:
                        return 0
        return 1

    result = []
    for i in range(5):
        result.append(main(places[i]))
    return result