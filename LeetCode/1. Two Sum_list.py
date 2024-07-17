#===========================================================================================================================
# Loop algorithm
class Solution:
    def twoSum(self, nums, target: int):
        for i in range(len(nums)):
            for j in range(i+1, len(nums)):
                if nums[i] + nums[j] == target:
                    return [i, j]
        return None
#===========================================================================================================================
# Two-pointer algorithm
def twoSum(nums, target) :
    nums.sort()
    l = 0
    r = len(nums)-1
    while l < r :
        if nums[l]+nums[r] == target :
            return True
        elif nums[l]+nums[r] > target :
            r -= 1
        else :
            l += 1
    return False
#===========================================================================================================================
# 재귀

#===========================================================================================================================
# 딕셔너리

#===========================================================================================================================
twoSum(nums=[4, 1, 9, 7, 5, 3, 16], target=14)
twoSum(nums=[2, 1, 5, 7], target=4)



def subsets(self, nums):
    def backtrack(start, path):
        result.append(path[:])
        
        for i in range(start, len(nums)):
                            
            path.append(nums[i])
            backtrack(i + 1, path)
            path.pop()

    result = []
    backtrack(0, [])
    return result