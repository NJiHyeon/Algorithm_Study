def solution(arrayA, arrayB):
    import math
    gcd_a = gcd_n(arrayA) 
    gcd_b = gcd_n(arrayB) 
    
    answer_a = gcd_n(arrayA) 
    answer_b = gcd_n(arrayB) 

    for a in arrayA: 
        if a % gcd_b == 0:
            answer_b = 0
            break
    for b in arrayB: 
        if b % gcd_a == 0:
            answer_a = 0
            break
    return max(answer_a, answer_b)

def gcd_2(m, n): 
    while n > 0 :
        m, n = n, m%n
    return m

def gcd_n(arr): 
    gcd = arr[0]
    for i in arr :
        gcd = gcd_2(gcd, i)
    return gcd
