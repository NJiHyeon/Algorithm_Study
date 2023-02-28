# 팩토리얼 ⭕ 
N = int(input())
def factorial(N) :
    if N <= 1 :
        return 1
    return N*factorial(N-1)

print(factorial(N))

#-------------------------------------------------------------
# 피보나치 수 ⭕
n = int(input())
def pibo(n) : 
    if n == 0 :
        return 0
    elif 1 <= n <= 2 :
        return 1
    else :
        return pibo(n-1) + pibo(n-2)
    
print(pibo(n))


#-------------------------------------------------------------
# 재귀의 귀재 ⭕
T = int(input())

def recursion(s, l, r) :
    global n
    n += 1
    if l >= r :
        return 1
    elif s[l] != s[r] :
        return 0
    else :
        return recursion(s, l+1, r-1)
    
def isPalindrome(s) :
    return recursion(s, 0, len(s)-1)

for i in range(T) :
    n = 0
    s = input()
    print(isPalindrome(s), n, sep=' ')
    

#-------------------------------------------------------------    
# 알고리즘 수업 - 병합정렬 1 ⭕
import sys
sys.setrecursionlimit(10**6)
# input() -> sys.stdin.readline()
N, K = map(int, sys.stdin.readline().split())
A = []
a = list(map(int, sys.stdin.readline().split()))


def merge_sort(a) :
    # 최소단위까지 쪼개지면 출력할 로직
    if len(a) == 1 :
        return a
    mid = (len(a)+1)//2
    left = merge_sort(a[:mid])
    right = merge_sort(a[mid:])
    
    L = []
    i, j = 0, 0
    while i < len(left) and j < len(right) :
        if left[i] < right[j] :
            L.append(left[i])
            A.append(left[i])
            i += 1
        else :
            L.append(right[j])
            A.append(right[j])
            j += 1
    
    while i < len(left) :
        L.append(left[i])
        A.append(left[i])
        i += 1
    
    while j < len(right) :
        L.append(right[j])
        A.append(right[j])
        j += 1
        
    return L

merge_sort(a)

if len(A) >= K : 
    print(A[K-1])
else :
    print(-1)
    
    
#-------------------------------------------------------------
# 별찍기 ❌
import sys
sys.setrecursionlimit(10**6)

N = int(sys.stdin.readline())

def star(N) :
    if N == 1 :
        return ['*']
    
    S = star(N//3)
    star_list = []
    
    for s in S :
        star_list.append(s*3)
    
    for s in S :
        star_list.append(s+ ' ' * (N//3)+ s)
    
    for s in S :
        star_list.append(s*3)
        
    return star_list

"""        
# 1) 시간 초과 발생
for i in range(N) :
    print(star(N)[i])
"""
   
# 2) 결과 정답
print('\n'.join(star(N)))


#-------------------------------------------------------------
# 하노이 탑 이동 순서 ❌
n = int(input())
k = 2**n - 1

def circle(n, a, b) :
    if n > 1 :
        circle(n-1, a, 6-a-b)
    
    print(a, b)
    if n > 1 :
        circle(n-1, 6-a-b, b)
    
print(k)
circle(n, 1, 3)
