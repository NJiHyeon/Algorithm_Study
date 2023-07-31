'''My code'''
location = input()
E = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h']
N = [1, 2, 3, 4, 5, 6, 7, 8, 9]
for e in range(8) :
    if location[0] == E[e] :
        l = str(N[e]) + str(location[1])
        
L = []
for i in l :
    L.append(int(i))
    
dx1 = [2, -2]
dy1 = [1, -1]
dx2 = [1, -1]
dy2 = [2, -2]
count = 0
for i in range(2) :
    for j in range(2) :
        nx = L[0] + dx1[i]
        ny = L[1] + dy1[j]
        if nx < 1 or ny < 1 or nx > 8 or ny > 8 : 
            continue
        else :
            count += 1
            
    
        nx = L[0] + dx2[i]
        ny = L[1] + dy2[j]
        if nx < 1 or ny < 1 or nx > 8 or ny > 8 : 
            continue
        else :
            count += 1  
            
print(count)


'''Lectuer code'''
# 현재 나이트의 위치 입력받기
input_data = input()
row = int(input_data[1])
column = int(ord(input_data[0])) - int(ord('a')) + 1

# 나이트가 이동할 수 있는 8가지 방향 정의
steps = [(-2, -1), (-1, -2), (1, -2), (2, -1), (2, 1), (1, 2), (-1, 2), (-2, 1)]

# 8가지 방향에 대하여 각 위치로 이동이 가능한지 확인
result = 0
for step in steps :
    # 이동하고자 하는 위치 확인
    next_row = row + step[0]
    next_column = column + step[1]
    # 해당 위치로 이동이 가능하다면 카운트 증가
    if next_row >= 1 and next_row <= 8 and next_column >= 1 and next_column <= 8 :
        result += 1
        
print(result)