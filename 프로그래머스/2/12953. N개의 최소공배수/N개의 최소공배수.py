def solution(arr):
    from math import gcd
    arr.sort()
    start = arr[0] #12
    for i in arr[1:] :
        g = gcd(start, i) #4
        start = g*(start//g)*(i//g)
    return start