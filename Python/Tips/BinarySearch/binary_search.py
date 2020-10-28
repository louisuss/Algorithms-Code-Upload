import bisect


def search(nums, target, start, end):
    while start <= end:
        mid = (start+end) // 2

        if nums[mid] == target:
            return mid
        elif nums[mid] < target:
            start = mid
        else:
            end = mid
    return -1


def search2(nums, target, start, end):
    if start <= end:
        mid = (start+end)//2

        if nums[mid] < target:
            search2(nums, target, mid+1, end)
        elif nums[mid] > target:
            search2(nums, target, start, mid-1)
        else:
            return mid
    else:
        return -1


def search3(nums, target, start, end):
    idx = bisect.bisect_left(nums, target)

    # bisect_left 이용시 인덱스 범위인지 체크 중요!
    if idx < len(nums) and nums[idx] == target:
        return idx
    return -1


def search4(nums, target):
    try:
        return nums.index(target)
    except ValueError:
        return -1


nums = [1, 3, 5, 6, 7, 8, 9, 14]
target = 8
print(search(nums, target, 0, len(nums)-1))
