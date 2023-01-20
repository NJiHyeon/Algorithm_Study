"""
내 풀이도 맞았지만 너무 길어진 것 같아서 다른 코드를 구글링 해보았다. 
조금 더 간결한 것 같지만 저렇게 바로 떠오를 수 있을까 하는 생각이 든다 ㅠㅠ
좀 더 쉽게 생각하려고 노력해보자 !!
"""
"""
2023/01/20
이전 내용들이랑 개념을 다시 복습하고 풀어보니
더 간단하게 풀렸당 !!~
"""
#----------------------------------------------------------------------------------------------------
# My code (다시!)
M = int(input())
N = int(input())
sosu_sum = 0 
sosu_min = []
 # 소수가 없으면 -1 출력
for i in range(M, N+1) :
    for x in range(2, i+1) :
        if i % x == 0 :
            if i == x :
                sosu_sum += i
                sosu_min.append(i)
            break

if sosu_sum == 0 :
    print("-1")
else :
    print(sosu_sum)
    # 숫자가 작은 순서로 들어가므로 젤 앞에 있는 것이 최솟값
    print(sosu_min[0])
    # 또는 print(min(sosu_min))

#----------------------------------------------------------------------------------------------------
# My Code(이전 코드)
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
    