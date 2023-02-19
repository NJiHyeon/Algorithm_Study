# 각 카드의 개수를 찾는 문제
# ----------------------------------------------------------------------------------
# 1) Collections 라이브러리의 Counter 함수 이용하기
# : 해당 요소들이 몇개가 있는지 자동으로 세어준다. 
import sys
from collections import Counter
_ = sys.stdin.readline()
N = sys.stdin.readline().split()
_ = sys.stdin.readline()
M = sys.stdin.readline().split()

C = Counter(N)

for m in M : 
    if m in C : 
        print(C[m], end=' ')
    else : 
        print(0, end=' ')

# --------------------------------------------------------------------------------
