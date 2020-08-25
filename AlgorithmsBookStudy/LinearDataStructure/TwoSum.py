# O(n**2)
def two_sum(nums, target):
    for i in range(len(nums)):
        for j in range(i+1, len(nums)):
            if nums[i] + nums[j] == target:
                return [i, j]

# O(n**2)


def two_sum2(nums, target):
    for i, n in enumerate(nums):
        complement = target - n

        if complement in nums[i+1:]:
            return nums.index(n), nums[i+1:].index(complement) + (i+1)

# O(n)


def two_sum3(nums, target):
    nums_map = {}
    for i, num in enumerate(nums):
        nums_map[num] = i

    for i, num in enumerate(nums):
        if target - num in nums_map and i != nums_map[target - num]:
            return nums.index(num), nums_map[target-num]

# O(n)


def two_sum4(nums, target):
    nums_map = {}
    for i, num in enumerate(nums):
        if target - num in nums_map:
            return [nums_map[target-num], i]
        nums_map[num] = i

# 투포인터 활용 -> 하지만 이 문제는 조건이 정렬안되어있음


def two_sum5(nums, target):
    # nums.sort() -> 인덱스가 엉망이됨
    left, right = 0, len(nums)-1
    while not left == right:
        if nums[left] + nums[right] < target:
            left += 1
        elif nums[left] + nums[right] > target:
            right -= 1
        else:
            return [left, right]
