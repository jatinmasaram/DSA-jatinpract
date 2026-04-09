def return_pairs(nums,target):
    freq = {}
    pairs = []

    for num in nums:
        complement = target - num

        if complement in freq:
            for _ in range(freq[complement]):
                pairs.append((complement, num))

        freq[num] = freq.get(num,0) + 1

    return pairs


print (return_pairs([2,3,2,1,4,2], 4))