def solution(info, edges):
    visited = [0 for _ in range(len(info))]
    answer = []

    def backtracking(sheep, wolf):
        # 탈출조건
        if sheep > wolf:
            answer.append(sheep)
        else:
            return

        # 반복수행
        for p, c in edges:
            if visited[p] and not visited[c]:
                visited[c] = True
                if info[c] == 0:
                    backtracking(sheep+1, wolf)
                else:
                    backtracking(sheep, wolf+1)
                visited[c] = False
    
    visited[0] = True
    backtracking(1, 0)

    return max(answer)