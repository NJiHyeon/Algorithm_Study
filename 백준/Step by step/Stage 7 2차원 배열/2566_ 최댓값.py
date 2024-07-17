# 최댓값을 2차원에서 찾는 문제
#-------------------------------------------------------------------------------------------
numbers = []
for row in range(9) :
    row = list(map(int, input().split()))
    numbers.append(row)
 
 
# max 주의 !! (최댓값이 0이 될 수도 있으므로 -1로 잡자 !)   
max = -1
r = 0
c = 0
for row in range(9) :
    for col in range(9) :
        if numbers[row][col] > max :
            max = numbers[row][col]
            r = row + 1
            c = col + 1
            
print(max)
print(r, c)