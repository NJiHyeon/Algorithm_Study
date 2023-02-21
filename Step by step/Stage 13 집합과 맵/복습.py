# 숫자카드 문제 : 두개의 문자열 집합을 비교하여 문자열 유무의 이진분류
## 방법1 : 기준 문자열 집합을 딕셔너리로 만들어서 검색 문자열 집합을 돌면서 딕셔너리에 있으면/없으면 출력 
import sys
N = int(sys.stdin.readline())
card = list(map(int, sys.stdin.readline().split()))
M = int(sys.stdin.readline())
check = list(map(int, sys.stdin.readline().split()))

diction = {}
for i in card :
    diction[i] = 0

for j in check :
    if j in diction :
        print(1, end=' ')
    else :
        print(0, end=' ')


## 방법2 : 이분탐색
import sys
N = int(sys.stdin.readline())
card = sorted(list(map(int, sys.stdin.readline().split())))
M = int(sys.stdin.readline())
check = list(map(int, sys.stdin.readline().split()))

def binary_s(num) :
    high, low = N-1, 0
    while low <= high :
        # mid는 값이 계속 바뀌어야 하므로 while문 아래
        mid = (low+high)//2
        if num < card[mid] :
            high = mid-1
        elif num > card[mid] :
            low = mid + 1
        else :
            return 1
    return 0

for i in range(M) : 
    binary_s(check[i])



## 방법3 : 자동함수(Counter)
import sys
N = int(sys.stdin.readline())
card = list(map(int, sys.stdin.readline().split()))
M = int(sys.stdin.readline())
check = list(map(int, sys.stdin.readline().split()))

from collections import Counter
c = Counter(card)
for i in check :
    if i in c :
        print(1, end=' ')
    else :
        print(0, end=' ')




#---------------------------------------------------------
# 문자열 집합 : 두개의 문자열을 비교하여 문자열 있는거 개수
import sys
from collections import Counter
N, M = map(int, sys.stdin.readline().split())
n_list = []
m_list = []
for i in range(N+M) :
    if i < N :
        n_list.append(sys.stdin.readline().strip())
    else :
        m_list.append(sys.stdin.readline().strip())

c = Counter(n_list)

n = 0
for j in m_list :
    if j in c :
        print(j)
        n += 1

print(n)


#---------------------------------------------------------
# 듣보잡 : 있는거 and 있는거 개수
import sys
from collections import Counter
N, M = map(int, sys.stdin.readline().split())
n_list = []
m_list = []
for i in range(N+M) :
    if i < N :
        n_list.append(sys.stdin.readline().strip())
    else :
        m_list.append(sys.stdin.readline().strip())

c_m = Counter(m_list)
n = 0
nm_list = []

for i in n_list :
    if i in c_m :
        n += 1
        nm_list.append(i)
        nm_list.sort()

print(n)
for k in nm_list :
    print(k)


#---------------------------------------------------------
# 대칭 차집합 : 있는거 빼고 없는거 개수
import sys
from collections import Counter
A, B = map(int, sys.stdin.readline().split())
a = list(map(int, sys.stdin.readline().split()))
b = list(map(int, sys.stdin.readline().split()))

c_a = Counter(a)
c_b = Counter(b)

n = 0

for i in a :
    if i not in c_b :
        n += 1

for j in b :
    if j not in c_a :
        n += 1

print(n)


#---------------------------------------------------------
# 서로 다른 부분 문자열의 개수 : 문자열을 새로 만들고 겹치는거 빼고 출력
import sys
from collections import Counter
S = sys.stdin.readline().strip()

s_list = []
for i in range(1, len(S)+1) :
    for j in range(len(S)) :
        s_list.append(S[j : j+i])

print(len(set(s_list)))


#---------------------------------------------------------
# 포켓몬 마스터 : 저장된 문자열 집합에서 입력(문자열 or 인덱스) -> 출력(인덱스 or 문자열)
import sys
from collections import Counter

N, M = map(int, sys.stdin.readline().split())
n_list = []
n_dict = {}

for i in range(N) :
    n_list.append(sys.stdin.readline().strip())
    
# 아이디어 출발 생각 
# 1) 딕셔너리로 만들어야 하는데 인덱스도 같이 저장되어야 한다!
# 2) 그러면 Counter로 자동으로 만들면 문자열, 개수만 저장되므로
# 3) 딕셔너리 {}를 직접 정의해서 추가해야 한다
# 4) 궁금한 M이 인덱스(숫자)로도 들어오고, 문자열로도 들어오므로 key값은 이 두가지를 모두 갖고 있어야 한다.

for i in range(N) :
    n_dict[str(i+1)] = n_list[i]
    n_dict[n_list[i]] = i+1

for _ in range(M) :
    print(n_dict[sys.stdin.readline().strip()])


# 그 후에 시간 좀 더 줄이려면,
# 1) for i in range(N)에서 두개의 반복문을 하나로 묶을 수 있음 !
