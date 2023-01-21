N = int(input())

for n in range(N) :
    number = int(input())
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
    for i in sosu_list[-1::-1] :
        for j in sosu_list[-1::-1] :
            if i + j == number and i<=j :
                
                #print(i, j, end=' ')
                #print()
                final_list.append(i)
                final_list.append(j)
    print(final_list[0], final_list[1], end=' ')
    print()

 




