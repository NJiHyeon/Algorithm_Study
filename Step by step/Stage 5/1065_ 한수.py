# X가 한수인지 판별하는 함수를 정의하여 문제를 해결해 봅시다.
N = int(input())
s = set()

if 0 < N < 100 : 
    s.add(N)
        
elif 100 <= N < 1000 :
    for i in range(1, 100) :
        s.add(i)
    
    for i in range(100, N+1) :
        a = str(i)
        if int(a[0])-int(a[1]) == int(a[1]) - int(a[2]) :
            s.add(i)

elif N == 1000 :
    for i in range(1, 100) :
        s.add(i)
    
    for i in range(100, 1000) :
        a = str(i)
        if int(a[0])-int(a[1]) == int(a[1]) - int(a[2]) :
            s.add(i)
            
print(len(s))
