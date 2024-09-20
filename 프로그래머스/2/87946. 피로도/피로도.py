def solution(k, dungeons):
    def backtracking(curr_d, curr_n, k):
        nonlocal result
        # 탈출 조건
        if k >= 0:
            result = max(result, curr_n)

        # 반복 수행
        for i in range(len(dungeons)):
            if i not in curr_d and dungeons[i][0] <= k:
                curr_d.append(i)
                k -= dungeons[i][1]
                curr_n += 1
                backtracking(curr_d, curr_n, k)
                curr_d.pop()
                k += dungeons[i][1]
                curr_n -= 1

    result = 0
    backtracking([], 0, k)
    return result