# 모든 경우를 시도하여 N의 생성자를 구하는 문제 ⭕
import sys
N = int(sys.stdin.readline())

n_list = []
for i in range(N) :
    n_len = int(len(str(i)))
    n_sum = i
    for k in range(n_len) :
        n_sum += int(str(i)[k])
    if n_sum == N :
        n_list.append(i)
    


if len(n_list) != 0 :
    print(n_list[0])
else :
    print(0)