def count_pairs(nums , target):

    freq = {}
    count = 0

    for num in nums:
        complement = target - num   # a+b=target or b=target-a

        if complement in freq:
            count = count + freq[complement]

        freq[num] = freq.get(num,0) + 1

    return count

print((count_pairs([2,3,2,2],4)))
