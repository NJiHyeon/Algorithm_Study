# 평균을 조작하는 문제
N = int(input())
score = list(map(int, input().split()))
l = []

for i in range(N) :
    s = (score[i]/max(score))*100
    l.append(s)
    
print(sum(l)/N)