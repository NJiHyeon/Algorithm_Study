# 모든 사람을 비교하여 덩치 등수를 구하는 문제
#------------------------------------------------------------------------------
import sys
n = int(sys.stdin.readline())
students = []
for i in range(n) :
    d = list(map(int, input().split()))
    students.append(d)
    
sum_rank = []
for i in range(n) :
    ranking = 1
    for j in range(n) :
        if students[i][0] < students[j][0] and students[i][1] < students[j][1] :
            ranking += 1
        
    sum_rank.append(ranking)
    
for i in sum_rank :
    print(i, end=' ')