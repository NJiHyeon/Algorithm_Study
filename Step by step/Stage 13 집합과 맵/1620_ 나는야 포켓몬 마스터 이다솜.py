# 맵을 사용하여 이름과 수를 연결짓는 문제
#------------------------------
# 처음 시도한 코드
import sys
N, M = map(int, sys.stdin.readline().split())
p_list = []  
for i in range(N+M) :
    if i < N : 
        name = input()
        p_list.append(name)
    else : 
        q = input()
        if q in p_list : 
            print(p_list.index(q) + 1)
        else : 
            print(p_list[int(q)-1])
        
#------------------------------
# 딕셔너리로 풀기
import sys
N, M = map(int, sys.stdin.readline().split())
p_dict = {}
for i in range(N) :
    name = input().rstrip()
    p_dict[i] = name
    p_dict[name] = i
    
for i in range(M) :
    q = input().rstrip()
    if q.isdigit() :
        print(p_dict[int(q)-1])
    else : 
        print(p_dict[q]+1)
