"""
15. 3Sum
Medium

Given an array nums of n integers, are there elements a, b, c in nums such that a + b + c = 0? Find all unique triplets in the array which gives the sum of zero.

Note:

The solution set must not contain duplicate triplets.

Example:

Given array nums = [-1, 0, 1, 2, -1, -4],

A solution set is:
[
  [-1, 0, 1],
  [-1, -1, 2]
]

Accepted
969,120
Submissions
3,619,249
"""

def in_list(nums, target):

    def twoSum(nums, target):
            seen = set()
            sol = []
            for i in range(len(nums)):
                to_find = target - nums[i]
                if to_find in seen and (to_find, nums[i]) not in sol:
                    sol.append((to_find, nums[i]))
                seen.add(nums[i])
            return sol
        
    nums.sort()
    solutions = []
    seen = set()
    
    for i in range(len(nums)-1):
        if nums[i] in seen:
            continue
        to_find = 0 - nums[i]
        combos = twoSum(nums[i+1:], to_find)
        if not combos:
            continue
        else:
            for num2, num3 in combos:
                solutions.append([nums[i], num2, num3])
        seen.add(nums[i])
    
    return solutions



    


        
    # solutions = []

    # targets = set()
        
    # i, j = 0, 1
    # while i <= len(nums) - 3:
    #     while j <= len(nums) - 2:
    #         target = 0 - nums[i] - nums[j]
    #         targets.add(set)
    #         triplet = sorted([nums[i], nums[j], target])
    #         if target in nums[j+1:] and triplet not in solutions:
    #             solutions.append(triplet)
    #         j += 1
    #     i += 1
    #     j = i + 1
    

print(threeSum([3,0,-2,-1,1,2]))
print(threeSum([0,0,0]))

"""
nums.sort() = [-2,-1,0,1,2,3]
solutions = []
i = 0
j = 3
length of nums = 6
len(nums) - 3 = 3
len(nums) - 2 = 4
nums[i] = 3
nums[j] = -1
nums[j+1:] = [1,2]
target = 0 - 3 + 1 == -2
triplets = [-2,-1,3]
"""
