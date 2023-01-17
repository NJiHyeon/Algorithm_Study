"""
내 풀이도 맞았지만 너무 길어진 것 같아서 다른 코드를 구글링 해보았다. 
조금 더 간결한 것 같지만 저렇게 바로 떠오를 수 있을까 하는 생각이 든다 ㅠㅠ
좀 더 쉽게 생각하려고 노력해보자 !!
"""
#----------------------------------------------------------------------------------------------------
# My Code
numbers = []
sosu = []
sosu_sum = 0
sosu_cnt = 0
M = int(input())
N = int(input())

while M <= N :
    numbers.append(M)
    M += 1

for x in numbers :
    for j in range(2, x+1) :
        if x%j == 0 :
            if x == j :
                sosu_cnt += 1
                sosu_sum += x
                sosu_min.append(x)
                sosu_min = sosu
            break

# 출력
if sosu_cnt == 0 :
    print(-1)
else :
    print(sosu_sum)
    print(sosu_min)   

#----------------------------------------------------------------------------------------------------
# Googling Code
M = int(input())
N = int(input())

sosu_list = []
for num in range(M, N+1): # M이상 ~ N이하의 수
    count = 0 # 나눠지는 수가 있으면 카운트
    if num > 1: # 2이상의 수들 중에 소수를 찾는다.
        for i in range(2, num): # 2~num에서 나눠지는 수를 찾는다
            if num % i == 0: # 나머지가 0이면 나눠지는 수(소수 아님)
                count += 1 # 소수가 아님을 카운트
                break
        if count == 0: # 나눠지는 수가 없으면 소수
            sosu_list.append(num)


if len(sosu_list) > 0:
    print(sum(sosu_list))
    print(min(sosu_list))
else:
    print(-1)
    
    
for i in range(2, 4) :
    print(i)