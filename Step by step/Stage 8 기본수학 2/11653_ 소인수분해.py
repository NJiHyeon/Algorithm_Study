"""
역시나 틀렸다..코드가 넘 지저분
먼저 2로 나누고 또 2로 나누는 수가 있는데 어떻게 ?? 했는데 바보같이
while 문을 돌려서 해당 수를 나눌 수 없을 때까지 돌리면 되는 거였다 !
"""
#----------------------------------------------------------------------------------------------------
# My Code - Incorrect 
N = int(input())
soinsu = []

for i in range(2, N+1) :
    if N%i == 0 :
        if N == i :
            print(i)
        else :
            soinsu.append(i)
            N = N/i
            
soinsu.append(int(N))          

for x in soinsu :
    for i in range(2, x+1) :
        if x%i == 0 :
            if x != i :
                soinsu.remove(x)
                soinsu.append(i)
                soinsu.append(x//i)
 
if N == 1:
    print("")
else :
    soinsu.sort()
    for x in soinsu :
        print(x)
#----------------------------------------------------------------------------------------------------
# Goggling Code
N = int(input())

if N == 1 :
    print("")
    
for x in range(2, N+1) :
    if N % x == 0 :
        while N % x == 0 :
            print(x)
            N = N / x