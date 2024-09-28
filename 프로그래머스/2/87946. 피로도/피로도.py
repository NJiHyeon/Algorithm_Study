def solution(k, dungeons):
    def backtracking(cur_k, cur_n, curr):
        # 탈출조건
        nonlocal result
        result = max(result, cur_n)

        # 반복수행
        for d in range(len(dungeons)):
            if d not in curr:
                if cur_k >= dungeons[d][0]:
                    curr.append(d)
                    cur_k -= dungeons[d][1]
                    cur_n += 1
                    backtracking(cur_k, cur_n, curr)
                    cur_k += dungeons[d][1]
                    cur_n -= 1
                    curr.pop()
    result = 0
    backtracking(k, 0, [])
    return result