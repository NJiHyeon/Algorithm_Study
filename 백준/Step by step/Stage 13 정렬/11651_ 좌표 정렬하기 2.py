# 좌표를 다른 순서로 정렬하는 문제(y좌표 먼저) ⭕
"""
앞 문제에서 .sort()를 하면 x좌표먼저 오름차순으로 정렬해주는데, y좌표 먼저 정렬을 하고 싶다.
리스트 안에 숫자가 2개로 정해져 있으니 인덱스를 바꿔서 정렬 해주고,
다시 바꿔서 출력하는 방향으로 생각했다. 
(범위가 크므로 sys는 필수로 해주었움, 입력을 받을 때 변수를 여러개 만들어서 넣고 넣고 하면 에러 발생 확률 높아지므로 한번에 만들도록, 빈 리스트도 꼭 만들어놓기)
"""
#--------------------------------------------------------------------------------------------
# My Code
import sys
N = int(sys.stdin.readline())
number_list = []
for i in range(N) :
    number_list.append(list(map(int, sys.stdin.readline().split())))

# change_list    
for i in number_list :
    i[0], i[1] = i[1], i[0]

number_list.sort()

for i in number_list :
    print(i[1], i[0], end=' ')
    print() # 줄넘김



#--------------------------------------------------------------------------------------------
# Googling Code