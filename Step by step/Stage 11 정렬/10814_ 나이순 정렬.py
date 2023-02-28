# 값이 같은 원소의 전후관계가 바뀌지 않는 정렬 알고리즘을 안정 정렬이라고 한다.
# 💡 # (age, name)에서 age만 비교
#--------------------------------------------------------------------------------------------
# My Code
N = int(input())
list = []
for i in range(N) :
    age, name = input().split()
    age = int(age)
    list.append([age, name])

for i in range(N-1) :
    if list[i][0] == list[i+1][0] :
        pass  
    else :
        if list[i][0] > list[i+1][0] :
            list[i], list[i+1] = list[i+1], list[i]

#--------------------------------------------------------------------------------------------
# Googling Code + My
"""
두개의 요소를 리스트로 묶는것 까지는 했는데, 하나만 비교하고 싶다는 생각이 들어서 
이를 나타내는 코드가 있을까 ? 하다가 구글링을 했더니 있었다 !
생소하지만 외워두면 좋을 것 같다.
"""
N = int(input())
a_list = []
for i in range(N) :
    age, name = input().split()
    age = int(age)
    a_list.append([age, name])
    
a_list.sort(key = lambda x : (x[0])) # (age, name)에서 age만 비교
a_list
for i in a_list :
    print(i[0], i[1])