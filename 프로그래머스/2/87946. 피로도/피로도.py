def solution(k, dungeons):
    def backtrack(visited, cur_k, cur_n):
        nonlocal max_n
        # base case
        if cur_n > max_n:
            max_n = cur_n
        # repeat
        for i in range(len(dungeons)):
            cur_d = dungeons[i]
            if i not in visited:
                if cur_k >= cur_d[0]:
                    cur_k -= cur_d[1]
                    cur_n += 1
                    visited.append(i)
                    backtrack(visited, cur_k, cur_n)
                    cur_k += cur_d[1]
                    cur_n -= 1
                    visited.pop()
                    
    max_n = 0
    backtrack([], k, 0)
    return max_n