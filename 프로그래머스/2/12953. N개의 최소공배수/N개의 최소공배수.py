def solution(arr):
    from math import gcd
    start = arr[0] 
    for i in arr[1:] :
        g = gcd(start, i) 
        start = g*(start//g)*(i//g) #start*i//g
    return start