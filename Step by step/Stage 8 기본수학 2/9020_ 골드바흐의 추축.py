# 시간초과 발생 ㅠㅠㅠ
N = int(input())

for n in range(N) :
    number = int(input())
    # 먼저 주어진 범위에서 소수만 구해서 리스트에 넣는다. 
    sosu_list = []
    for i in range(1,number+1):
        if i==1:#1은 소수가 아니므로 제외
            continue
  
        for j in range(2,int(i**0.5)+1):
            if i%j==0: 
             break   
        else:
            sosu_list.append(i)
    
    
    final_list = []
    # 역순으로 바꾸기
    for i in sosu_list[-1::-1] :
        for j in sosu_list[-1::-1] :
            if i + j == number and i<=j :
                
                #print(i, j, end=' ')
                #print()
                final_list.append(i)
                final_list.append(j)
    print(final_list[0], final_list[1], end=' ')
    print()

#-------------------------------------------------------------------------------
# Googling code
sosu = [0 for i in range(10001)]
sosu[0] = 1
sosu[1] = 1
for i in range(2, 101) :
    for j in range(i+i, 10001, i) :
        sosu[j] = 1
        
t = int(input())
for i in range(t) :
    a = int(input())
    b = a//2
    for j in range(b, 1, -1) :
        if sosu[a-j] == 0 and sosu[j] == 0 :
            print(j, a-j)
            break




