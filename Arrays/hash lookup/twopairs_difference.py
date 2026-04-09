def has_difference(nums,k):
    seen ={}

    for sub in nums:
        a = sub + k

        if a in seen:
            return True
        seen[a]=True
    return False
    
print(has_difference([1,5,3,4,2],2))