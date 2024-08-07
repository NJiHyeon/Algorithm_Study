nums = [2,7,11,15]
target = 9

nums_dict = {}

for i, num in enumerate(nums):
    if target-num in nums_dict:
        print([nums_dict[target-num], i])
    nums_dict[num] = i