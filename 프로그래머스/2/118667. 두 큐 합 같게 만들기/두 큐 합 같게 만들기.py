def solution(queue1, queue2):
    l = 0
    r = len(queue1)
    n = 0
    N = len(queue1) + len(queue2)
    target = (sum(queue1) + sum(queue2)) // 2
    queue = queue1 + queue2
    cur_sum = sum(queue[l:r])
    
    while n < 2*N:
        if cur_sum == target:
            return n
        elif cur_sum < target:
            cur_sum += queue[r]
            r += 1
            r %= N
        elif cur_sum > target:
            cur_sum -= queue[l]
            l += 1
            l %= N
        n += 1
    return -1