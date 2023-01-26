# 5개의 수의 평균과 중앙값을 구하는 문제
#------------------------------------------------------------------------------
# My Code
number_list = []
total = 0
for _ in range(5) :
    number = int(input())
    number_list.append(number)
    total += number
    
number_list.sort()
print(int(total/5))
print(number_list[2])



#------------------------------------------------------------------------------
# Googling Code