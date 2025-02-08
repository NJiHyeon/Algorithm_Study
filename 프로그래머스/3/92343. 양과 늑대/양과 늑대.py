def solution(info, edges):
    def backtracking(sheep, wolf):
        # base case
        if sheep > wolf:
            result.append(sheep)
        else:
            return
        
        # repeat
        for edge in edges:
            if visit[edge[0]] == True and visit[edge[1]] == False:
                visit[edge[1]] = True
                if info[edge[1]] == 0:
                    backtracking(sheep+1, wolf)
                else:
                    backtracking(sheep, wolf+1)
                visit[edge[1]] = False
                
    result = []
    visit = [False for _ in range(len(info))]
    visit[0] = True
    backtracking(1, 0)
    return max(result)