# 좌표를 정렬하는 문제 ⭕
#--------------------------------------------------------------------------------------------
# My Code
import sys
N = int(sys.stdin.readline())

dot_list = []
for i in range(N) :
    dot_list.append(list(map(int, sys.stdin.readline().split())))

dot_list.sort()
dot_list
for i in dot_list :
    print(i[0], i[1], end= '')
    print()


#--------------------------------------------------------------------------------------------
# Googling Code