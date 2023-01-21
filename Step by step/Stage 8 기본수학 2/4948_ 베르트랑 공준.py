# 시간초과 발생
# 모든 숫자를 for, while 돌면서 소수를 구했기 때문
sosu_list = []
while True :
    n = int(input())
    if n == 0 :
        break
    else :
        sosu_no = 0
        for x in range(n+1, 2*n + 1) :
            for i in range(2, int(x**0.5)+1) :
                if x % i == 0 :
                    sosu_no += 1
                    break
        sosu_cnt = n - sosu_no
        sosu_list.append(sosu_cnt)
       
for i in sosu_list :
    print(i)

#---------------------------------------------------------
# 주어진 범위 사이에서 소수를 모두 구해놓고, 입력받은 숫자 사이에서 소수의 개수를 출력하도록 구한다. 
num = 123456*2+1
num_list = [1]*num
for i in range(1, num):
    if i == 1:
        continue
    for j in range(2, int(i**0.5)+1):
        if i % j == 0:
            num_list[i] = 0
            break

while True:
    n = int(input())
    prime = 0
    
    if n == 0:
        break
    
    # else도 넣어보기
    for i in range(n+1, 2*n+1):
            # 소수면 1이 더해지고 소수가 아니면 0이 더해진다. 
            prime += num_list[i]
    print(prime)