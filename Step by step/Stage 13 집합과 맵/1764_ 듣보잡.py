# --------------------------------------------------
import sys
N, M = map(int, sys.stdin.readline().split())

n_list = []
for i in range(N) :
    n = sys.stdin.readline().strip()
    n_list.append(n)
    
m_list = []
for j in range(M) :
    m = sys.stdin.readline().strip()
    m_list.append(m)
    
    
nm = 0
nm_list = []
for k in n_list :
    if k in m_list : 
        nm += 1
        nm_list.append(k)
        nm_list.sort()
        
print(nm)
for l in nm_list :
    print(l)


# --------------------------------------------------
# 리스트로 입력받은 값들을 Counter를 이용해서 딕셔너리로 만들었다. 그리고 나서 하나씩 비교하면서 출력!
import sys
from collections import Counter
N, M = map(int, sys.stdin.readline().split())
name_list = []
for i in range(N+M) :
    name = sys.stdin.readline().strip()
    name_list.append(name)

C = Counter(name_list)
db = 0
db_list = []
for i in C :
    if C[i] > 1 :
        db += 1
        db_list.append(i)
        db_list.sort()
    
print(db)
for i in db_list :
    print(i)
    