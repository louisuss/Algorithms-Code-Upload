def maxSubArr(nums):
    sums = [nums[0]]
    for i in range(1, len(sums)):
        sums.append(nums[i] + (sums[i-1] if sums[i-1] > 0 else 0))
    return max(sum)
