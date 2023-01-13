# 배열을 입력받고 v를 찾는 문제
n = int(input())
data = list(map(int, input().split()))
v = int(input())
print(data.count(v))