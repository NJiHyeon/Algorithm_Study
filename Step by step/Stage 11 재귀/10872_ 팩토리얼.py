# 팩토리얼은 단순 for문으로도 구할 수 있지만, 재귀함수로도 가능하다 !
#--------------------------------------------------------------------------------------------
# My Code
n = int(input())

def recursion(n) :
    if n == 0 :
        print(n)
    n *= n
    return recursion(n-1)
    
recursion(10)      
print()