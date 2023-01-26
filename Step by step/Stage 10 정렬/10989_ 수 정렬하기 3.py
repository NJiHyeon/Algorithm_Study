# 수의 범위가 작다면 카운팅 정렬을 사용하여 더욱 빠르게 정렬할 수 있다. 
import sys
n = int(sys.stdin.readline())
b = [0] * 10001

for i in range(n) :
    b[int(sys.stdin.readline())] += 1
    
for i in range(10001) :
    if b[i] != 0 :
        for j in range(b[i]) :
            print(i)
            