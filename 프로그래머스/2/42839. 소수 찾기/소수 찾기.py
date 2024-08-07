def solution(numbers):
    from itertools import permutations
    answer = 0
    nums = list(numbers)
    l = []
    for i in range(1, len(numbers)+1) :
        for j in permutations(nums, i) :
            st = ''
            for k in j :
                st += k
            if int(st)!=0 and int(st)!=1 and sosu(int(st)) == True :
                l.append(int(st))
    l = list(set(l))
    return len(l)

def sosu(n) :
    import math
    for i in range(2, int(math.sqrt(n))+1) :
        if n%i == 0 :
            return False
    return True