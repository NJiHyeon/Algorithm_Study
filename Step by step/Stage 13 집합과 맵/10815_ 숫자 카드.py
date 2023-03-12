# 카드의 집합을 만들어 특정 카드가 집합에 있는지 빠르게 찾는 문제
# 시간초과 발생
import sys
N = int(sys.stdin.readline())
n_list = list(map(int, sys.stdin.readline().split()))
M = int(sys.stdin.readline())
m_list = list(map(int, sys.stdin.readline().split()))

for i in m_list :
    if i in n_list :
        print(1, end=' ')
    else :
        print(0, end=' ')
        
#  ---------------------------------------------
# 방법1 : 딕셔너리 이용
import sys
N = int(sys.stdin.readline())
n_list = list(map(int, sys.stdin.readline().split()))
M = int(sys.stdin.readline())
m_list = list(map(int, sys.stdin.readline().split()))

diction = {}
for i in range(len(n_list)) :
    # 아무 숫자로 mapping
    diction[n_list[i]] = 0
    
for j in range(M) :
    if m_list[j] in diction :
        print(1, end=' ')
    else :
        print(0, end=' ')
        
#  ---------------------------------------------
# 방법2 : 이진(분) 탐색
import sys
N = int(sys.stdin.readline())
cards = sorted(list(map(int, sys.stdin.readline().split())))
M = int(sys.stdin.readline())
checks = list(map(int, sys.stdin.readline().split()))

for check in checks :
    low, high = 0, N-1
    exist = False
    while low <= high :
        mid = (low+high)//2
        if cards[mid] > check :
            high = mid - 1
        elif cards[mid] < check :
            low = mid + 1
        else :
            exist = True
            break
    print(1 if exist else 0, end=' ')
    
#  ---------------------------------------------
# + 이진 탐색(함수 사용)
import sys
N = int(sys.stdin.readline())
cards = sorted(list(map(int, sys.stdin.readline().split())))
cards.sort()

def binary_search(num) :
    l = 0
    h = N-1
    while l <= h :
        mid = (l+h)//2
        if cards[mid] > num :
            h = mid - 1
        elif cards[mid] < num :
            l = mid + 1
        else :
            return 1
    return 0

