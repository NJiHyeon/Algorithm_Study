def solution(x):
    x_list = list(map(int, str(x)))
    x_sum = 0
    for i in x_list :
        x_sum += i
    if x%x_sum == 0 :
        answer = True
    else :
        answer = False
    return answer

# 좋은코드
'''
def solution(n) :
    return n%sum(int(x) for x in str(n)) == 0
print(solution(18))
'''