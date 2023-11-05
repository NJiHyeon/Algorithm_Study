from  math import sqrt

def solution(n):
    point = int(sqrt(n))
    answer = -1
    for i in range(1, point+1) :
        if i*i == n :
            answer = (i+1)*(i+1)

    return answer


#---------
# 참고 코드 추가
'''
def solution(n):
    sqrt = n ** (1/2)

    if sqrt % 1 == 0:
        return (sqrt + 1) ** 2
    return '-1'
'''