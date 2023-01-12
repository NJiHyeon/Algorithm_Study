import sys
import math

# input()으로 하면 런타임 에러 발생
# 아래의 코드로 입력받기
A, B, V = map(int, sys.stdin.readline().split())
day = (V-B)/(A-B)
print(math.ceil(day))