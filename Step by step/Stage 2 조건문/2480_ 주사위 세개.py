a = input()
A = int(a[0])
B = int(a[2])
C = int(a[4])

if A == B == C :
    print(10000+A*1000)
elif (A==B) or (B==C) or (A==C) :
    if A==B : 
        print(1000+A*100)
    elif B==C :
        print(1000+B*100)
    else :
        print(1000 + C*100)
else :
    if A > B :
        if A > C :
            print(A*100)
        else : 
            print(C*100)
    elif B > A :
        if B > C :
            print(B*100)
        else :
            print(C*100)