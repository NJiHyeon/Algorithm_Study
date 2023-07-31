# 배열을 활용하여 서로 다른 값의 개수를 찾는 문제

l = []
for i in range(10) :
    n = int(input())
    l.append(n%42)
l = set(l)
print(len(l))