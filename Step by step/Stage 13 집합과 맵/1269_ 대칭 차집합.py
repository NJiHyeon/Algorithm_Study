# 둘 중 한 집합에만 속하는 원소를 모두 구하는 문제 ⭕
    # 리스트로 입력을 받아서 하나의 리스트로 묶고 이것을 딕셔너리로 바꾼다 !
    # 차집합은 딕셔너리에서 개수가 하나인 숫자인 것이므로 딕셔너리를 돌면서 값이 1인 개수를 구한다. 
import sys
from collections import Counter
A, B = map(int, sys.stdin.readline().split())
a = list(map(int, sys.stdin.readline().split()))
b = list(map(int, sys.stdin.readline().split()))

ab_list = []
for i in a :
    ab_list.append(i)
for j in b :
    ab_list.append(j)
C = Counter(ab_list)

cha = 0
for k in C :
    if C[k] == 1 :
       cha += 1 

print(cha)


