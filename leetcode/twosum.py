def twoSum(nums, target):
    

    
    sorted_nums = sorted(nums[:target])
    
    index = 0
    print(sorted_nums)
    for num in sorted_nums:
        find_num = 0 if target == 0 else target - num
        print(find_num)
        if (find_num) in sorted_nums[index+1:]:
            i = nums.index(num)
            print(i)
            return [i, nums.index(find_num, i+1)]
        index += 1
            