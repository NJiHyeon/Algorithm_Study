X = int(input())
N = int(input())
w = 0
for i in range(N) :
    a, b = map(int, input().split())
    w = w + a*b 
if w == X :
    print("Yes")
else :
    print("No")
