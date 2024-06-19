def solution(n):
    go = 0
    while n!=1 :
        if n%2==1 :
            n-=1
            go+=1
            n=n//2
        else :
            n=n//2
        
    return go+1