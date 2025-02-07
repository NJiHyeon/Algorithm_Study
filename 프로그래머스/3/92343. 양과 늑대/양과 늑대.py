def solution(info, edges):
    visit = [False for _ in range(len(info))]
    result = []
    def backtrack(sheep, wolf):
        if sheep > wolf:
            result.append(sheep)
        else:
            return
        
        for edge in edges:
            if visit[edge[0]] == True and visit[edge[1]] == False:
                if info[edge[1]] == 0:
                    visit[edge[1]] = True
                    backtrack(sheep+1, wolf)
                    visit[edge[1]] = False
                else:
                    visit[edge[1]] = True
                    backtrack(sheep, wolf+1)
                    visit[edge[1]] = False
    visit[0] = True
    backtrack(1, 0)
    return max(result)