# 시간 복잡도가 O(n^2)인 정렬 알고리즘으로 풀 수 있다. (예를 들면 삽입 정렬, 거품 정렬 등)
n = int(input())
n_list = []
for _ in range(n) :
    number = int(input())
    n_list.append(number)
    
n_list.sort()

for i in range(n) :
    print(n_list[i])
    
#-----------------------------------------------------------------------------------
# Googling Code 
# 버블 정렬 : 현재 값과 다음 인덱스의 값을 비교해서, 다음 인덱스 값이 현재 값보다 작으면 두 값을 서로 교환
n = int(input())
nums = []
for _ in range(n) :
    nums.append(int(input()))
    
for i in range(len(nums)) :
    for j in range(len(nums) - i - 1) :
        if nums[j] > nums[j+1] :
            nums[j], nums[j+1] = nums[j+1], nums[j]
            
for k in nums :
    print(k)


# 삽입 정렬 : 이전 인덱스의 값과 현재 인덱스의 값을 비교해 작은 값을 앞으로 옮긴다. 
n = int(input())
nums = []
for _ in range(n) :
    nums.append(int(input()))
    
for i in range(1, len(nums)) :
    for j in range(i, 0, -1) :
        if nums[j] < nums[j-1] :
            nums[j], nums[j-1] = nums[j-1], nums[j]
            
for k in nums :
    print(k)