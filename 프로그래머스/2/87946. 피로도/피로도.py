def solution(k, dungeons):
    final_result = 0
    # 1. 순서를 담은 순열
    permutations = []
    def backtracking(curr):
        if len(curr) == len(dungeons):
            permutations.append(curr[:])
            return
        for i in range(len(dungeons)):
            if i not in curr:
                curr.append(i)
                backtracking(curr)
                curr.pop()
    backtracking([])
    # 2. 탐험할 수 있는 최대 던전 개수
    for permut in permutations:
        current = k
        result = 0
        for i in permut:
            if current >= dungeons[i][0]:
                current -= dungeons[i][1]
                result += 1
        if result > final_result:
            final_result = result
    return final_result
        