from itertools import combinations
import math

def solution(nums):
    sosu_n = 0
    combi = list(combinations(nums, 3))
    sums = []
    for c in combi :
        sums.append(sum(c))
    #sums = list(set(sums))
    
    for s in sums :
        if sosu(s) == True :
            sosu_n += 1
    return sosu_n


def sosu(n) :
    h = int(math.sqrt(n))
    for i in range(2, h+1) :
        if n%i == 0 :
            return False
    return True
    