"""
시간 초과 뜸 ...ㅠㅠ 항상 입력받는 숫자의 범위를 잘 보자.
"""
# 한 줄에 하나씩, 증가하는 순서대로 소수를 출력한다.
    # 입력 : 3 16
    # 출력 : 3 \n 5 \n 7 \n 11 \n 13

M, N = map(int, input().split())
for x in range(M, N+1) :
    for i in range(2, int(x**0.5)+1) :
        if x % i == 0 :
            
            if x == i :
                # print(x)
                
    #break : 소수도 고려안하고, 맨 처음 숫자 출력하고 끝
        #break : 아무것도 출력 안하고 끝
            # break 안하면 반복문만큼 돈다. (if 고려하지 않음 !!)
            # break
                # break : 전체 숫자 모두 출력
#------------------------------------------------------------------------------
# googling code
m,n=map(int,input().split())

for i in range(m,n+1):
    if i==1:#1은 소수가 아니므로 제외
        continue
    # 특정 수의 제곱근을 구해, 그 제곱근까지의 약수를 구하면 
    # 해당 약수를 포함하는 수를 모두 제거할 수 있다(소수가 아니므로).
    for j in range(2,int(i**0.5)+1):
        if i%j==0: #약수가 존재하므로 소수가 아님
            # 여기서는 if i==j :를 못쓴다.(제곱근을 했으니까 같은 숫자까지 돌지 않음 !)
            break   #더이상 검사할 필요가 없으므로 멈춤
    else:
        print(i)
          
#------------------------------------------------------------------------------
