def solution(k, dungeons):
    answer = 0
    def backtrack(visited, k):
        nonlocal answer
        # base case
        if len(visited) > answer:
            answer = len(visited)
        # repeat
        for i in range(len(dungeons)):
            if i not in visited:
                if k >= dungeons[i][0]:
                    # append
                    visited.append(i)
                    # call
                    backtrack(visited, k-dungeons[i][1])
                    # pop
                    visited.pop()
        return answer
    return backtrack([], k)