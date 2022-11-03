A, B = map(int, input().split())
if B >= 45 : 
    print(A, B-45)
else : 
    if A >= 1: 
        print(A-1, 60+B-45)
    else : 
        print(24+A-1, 60+B-45)