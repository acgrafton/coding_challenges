def twoSum(nums, target):
    
    seen_dict = {}
        
    for i, num in enumerate(nums):
        to_find = target - num
        if to_find in seen_dict:
            return (seen_dict[to_find], i)
        seen_dict[num] = i
            