def solution(info, edges):
    result = []
    visit = [False] * len(info)
    
    def backtracking(sheep, wolf):
        # 탈출조건
        if sheep > wolf:
            result.append(sheep)
        else:
            return
        # 반복수행
        for edge in edges:
            if visit[edge[0]] == True and visit[edge[1]] == False:
                if info[edge[1]] == 0:
                    visit[edge[1]] = True
                    backtracking(sheep+1, wolf)
                    visit[edge[1]] = False
                else:
                    visit[edge[1]] = True
                    backtracking(sheep, wolf+1)
                    visit[edge[1]] = False
    visit[0] = True
    backtracking(1, 0)
    return max(result)