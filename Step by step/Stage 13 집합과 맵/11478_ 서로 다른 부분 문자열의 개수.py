# 집합을 활용하여 중복을 제거하는 문제
# ------------------------------------------------------
import sys

S = sys.stdin.readline().strip()
cha = []
for i in range(1, len(S)+1) :
    for j in range(len(S)) :
        s = S[j:j+i]
        cha.append(s)


print(len(set(cha)))
