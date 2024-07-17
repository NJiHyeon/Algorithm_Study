# 만약 정확한 값이 필요 없고, 값의 대소 관계만 필요하다면, 모든 수를 0이상 N 미만의 수로 바꿀 수 있다. (최빈값 문제랑 비슷한 아이디어인듯)
# 💡 딕셔너리
#--------------------------------------------------------------------------------------------
# My Code 시간초과.....
import sys
N = int(sys.stdin.readline())
n_list = list(map(int, sys.stdin.readline().split()))
set_list = list(set(n_list))
final_list = []
for i in n_list :
    n = 0
    for j in set_list :
        if i > j :
            n += 1
    final_list.append(n)

for i in final_list :
    print(i, end=' ')
#--------------------------------------------------------------------------------------------
# Googling Code
import sys
N = int(sys.stdin.readline())
n_list = list(map(int, sys.stdin.readline().split()))
set_list = sorted(list(set(n_list))) # sorted 추가

# 딕셔너리 만들기
# 하나씩 비교해가면서 더하고 출력하면 시간초과가 발생한다.
# 따라서 딕셔너리를 만들고, 순서대로 정렬해서 인덱스만큼만 출력해주면 된다. !
dic = {set_list[i] : i for i in range(len(set_list))}
for i in n_list :
    print(dic[i], end=' ')