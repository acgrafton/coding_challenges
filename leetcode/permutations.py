def permute(nums):
        if len(nums) <= 1:
            return [nums]
        
        if len(nums) == 2:
            return [[nums[0], nums[1]], [nums[1], nums[0]]]
        
        nums_excl_self = [[]]

        i = 1
        while i < len(nums):
            nums_excl_self.append(nums_excl_self[i-1] + [nums[i-1]])
            i += 1
        
        j = len(nums) - 2
        seen = []
        while j >= 0:
            seen.append(nums[j+1])
            nums_excl_self[j].extend(seen)
            j -= 1
        
        print(nums_excl_self)
        permutations = []
        for i, num in enumerate(nums):
            for sub_permute in permute(nums_excl_self[i]):
                new = [num]
                new.extend(sub_permute)
                permutations.append(new)
                
        print(permutations)

permute([1,2,3,4])

    
            