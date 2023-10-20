import math
def solution(n):
    sosu_n = 0
    for i in range(2, n+1) :
        if sosu(i) == True :
            sosu_n += 1
    return sosu_n

def sosu(s) :
    h = int(math.sqrt(s))
    for i in range(2, h+1) :
        if s%i == 0 :
            return False
    return True