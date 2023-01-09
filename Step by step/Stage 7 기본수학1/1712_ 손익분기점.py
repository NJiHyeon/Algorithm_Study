# 이익이 발생하는 지점을 찾는 문제

A, B, C = map(int, input().split())

if B>=C:
    print(-1)
else:
    print(int(A/(C-B)+1))
