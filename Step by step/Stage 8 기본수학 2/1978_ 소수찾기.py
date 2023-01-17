# 2부터 X-1까지 모두 나눠서 X가 소수인지 판별하는 문제 1
n = int(input())
numbers = list(map(int, input().split()))
sosu = 0

for x in numbers :
    for i in range(2, x+1) :
        if x%i == 0 :
            if x == i :
                sosu += 1
            break
        
print(sosu)
                         
            
        