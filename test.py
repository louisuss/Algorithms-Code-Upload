def search(nums, target):
    # 예외 처리
    if not nums:
        return -1

    # 최솟값을 찾아 피벗 설정
    # pivot = nums.index(min(nums))
    left, right = 0, len(nums)-1
    while left < right:
        mid = left + (right-left)//2
        if nums[mid] > nums[right]:
            left = mid + 1
        else:
            right = mid
        print(left, right, mid)
    pivot = left

nums = [4,5,8,1,2,3,6,7]
target = 1

search(nums,target)