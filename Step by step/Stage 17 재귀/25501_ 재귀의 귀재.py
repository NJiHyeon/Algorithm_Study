# 재귀의 동작을 파악하는 문제
# -----------------------------------------------------------------------------------------
def recursion(s, l, r):
    global n
    n += 1
    if l >= r: return 1
    elif s[l] != s[r]: return 0
    else: return recursion(s, l+1, r-1)

def isPalindrome(s):
    return recursion(s, 0, len(s)-1)

N = int(input())
for i in range(N) :
    s = input()
    n = 0
    print(isPalindrome(s), n, end=' ')