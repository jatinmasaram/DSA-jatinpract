def count_pairs(nums, target):
    seen ={}


    for i , num in enumerate(nums):
        complement = target - num

        if complement in seen:
            return [seen[num],i]
        
        seen[num] = i

    return []
        
