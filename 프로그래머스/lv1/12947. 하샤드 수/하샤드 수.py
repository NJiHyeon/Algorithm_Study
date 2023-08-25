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