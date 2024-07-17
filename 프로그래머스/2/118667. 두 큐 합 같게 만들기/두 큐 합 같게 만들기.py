def solution(queue1, queue2):
    result = 0
    queue = queue1 + queue2
    l = 0
    r = len(queue)//2
    n = len(queue)
    total_sum = sum(queue)
    
    left_sum = sum(queue[l:r])
    right_sum = total_sum-left_sum
    
    while result < 4*len(queue):
        if left_sum < right_sum:
            right_sum -= queue[r]
            left_sum += queue[r]
            r += 1
            r %= n
            result += 1
        elif left_sum > right_sum:
            left_sum -= queue[l]
            right_sum += queue[l]
            l += 1
            l %= n
            result += 1
        else:
            return result
    return -1
            
            
    
#     while result < 4*(len(queue)):
#         left_sum = sum(queue[l:r])
#         right_sum = total_sum-left_sum
        
#         if left_sum < right_sum:
#             r += 1
#             result += 1
#         elif left_sum > right_sum:
#             l += 1
#             result += 1
#         else:
#             return result
#     return -1
        